from collections.abc import Iterator
from itertools import product
from urllib.parse import urlencode

from sitemapr.models import Page, Param, SiteMapUrl


class SiteMapr:
    def __init__(self, base_url: str, pages: list[Page]):
        self._base_url = base_url
        self._pages = pages

    def save(self, path: str) -> None:
        with open(path, "w") as f:
            f.write(
                '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            )
            for url in self.iter_urls():
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
            yield SiteMapUrl(loc=loc)

    def _get_param_combinations(
        self, params: list[Param] | None
    ) -> list[dict[str, str]]:
        if not params:
            return [{}]

        combinations: list[dict[str, str]] = []
        for values in product(*[param.values for param in params]):
            combination = {
                param.name: value for param, value in zip(params, values, strict=False)
            }
            combinations.append(combination)
        return combinations
