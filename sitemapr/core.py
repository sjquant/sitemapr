from collections.abc import Iterator
from io import TextIOWrapper
from itertools import product
from urllib.parse import urlencode

from sitemapr.models import Page, Param, SiteMapUrl


class SiteMapr:
    """
    A class for generating and saving sitemaps.

    Args:
        base_url: The base URL of the website.
        pages: A list of Page objects representing the pages to include in the sitemap.
        sitemap_base_url: The base URL for the sitemap. Defaults to None, which uses the base_url.
    """

    def __init__(
        self, base_url: str, pages: list[Page], *, sitemap_base_url: str | None = None
    ):
        self._base_url = base_url
        self._sitemap_base_url = sitemap_base_url or base_url
        self._pages = pages

    def save(self, dirname: str, *, chunk_size: int = 50000) -> None:
        """
        Save the sitemap to the specified directory.

        Args:
            dirname: The directory path where the sitemap will be saved.
            chunk_size: The number of URLs to include in each chunk. Defaults to 50000.
        """
        chunk: list[SiteMapUrl] = []
        idx = 0
        for url in self.iter_urls():
            if len(chunk) == chunk_size:
                self._save_chunk(dirname, idx, chunk)
                idx += 1
                chunk.clear()

            chunk.append(url)

        if not chunk:
            return

        if idx == 0:
            with open(f"{dirname}/sitemap.xml", "w") as f:
                self._write_urls(f, chunk)
        else:
            self._save_chunk(dirname, idx, chunk)

        if idx > 0:
            self._write_index_file(dirname, idx)

    def _save_chunk(self, dirname: str, idx: int, chunk: list[SiteMapUrl]) -> None:
        with open(f"{dirname}/sitemap-{idx}.xml", "w") as f:
            self._write_urls(f, chunk)

    def _write_index_file(self, dirname: str, idx: int) -> None:
        with open(f"{dirname}/sitemap.xml", "w") as f:
            f.write(
                '<?xml version="1.0" encoding="UTF-8"?><sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            )
            for i in range(idx + 1):
                f.write(
                    f"<sitemap><loc>{self._sitemap_base_url}/sitemap-{i}.xml</loc></sitemap>"
                )
            f.write("</sitemapindex>")

    def _write_urls(self, f: TextIOWrapper, urls: list[SiteMapUrl]):
        f.write(
            '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        )
        for url in urls:
            f.write(f"<url><loc>{url.loc}</loc>")
            if url.lastmod:
                f.write(f"<lastmod>{url.lastmod}</lastmod>")
            if url.changefreq:
                f.write(f"<changefreq>{url.changefreq}</changefreq>")
            if url.priority:
                f.write(f"<priority>{url.priority}</priority>")
            f.write("</url>")
        f.write("</urlset>")

    def iter_urls(self) -> Iterator[SiteMapUrl]:
        """
        Iterates over the URLs in the sitemap.

        Yields:
            SiteMapUrl: A SiteMapUrl object representing a URL in the sitemap.
        """
        for page in self._pages:
            yield from self._iter_page(page)

    def _iter_page(self, page: Page) -> Iterator[SiteMapUrl]:
        query_param_combinations = self._get_param_combinations(page.query_params)
        path_param_combinations: list[dict[str, str]] = self._get_param_combinations(
            page.path_params
        )
        for query_params, path_params in product(
            query_param_combinations, path_param_combinations
        ):
            path = page.path.format(**path_params)
            query_string = urlencode(query_params)
            loc = (
                f"{self._base_url}{path}?{query_string}"
                if query_string
                else f"{self._base_url}{path}"
            )
            yield SiteMapUrl(
                loc=loc,
                lastmod=page.lastmod,
                changefreq=page.changefreq,
                priority=page.priority,
            )

    def _get_param_combinations(
        self, params: list[Param] | None
    ) -> list[dict[str, str]]:
        if not params:
            return [{}]

        combinations: list[dict[str, str]] = []
        for values in product(*[param.values for param in params if param.values]):
            combination = {
                param.name: value for param, value in zip(params, values, strict=False)
            }
            combinations.append(combination)
        return combinations
