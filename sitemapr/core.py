from itertools import product
from urllib.parse import urlencode

from sitemapr.models import Page, Param, SiteMapUrl


class SiteMapr:
    def __init__(self, base_url: str, pages: list[Page]):
        self._base_url = base_url
        self._pages = pages

    def generate(self) -> list[SiteMapUrl]:
        urls: list[SiteMapUrl] = []
        for page in self._pages:
            page_urls = self._generate_page_urls(page)
            urls.extend(page_urls)
        return urls

    def _generate_page_urls(self, page: Page) -> list[SiteMapUrl]:
        urls: list[SiteMapUrl] = []
        query_param_combinations = self._get_param_combinations(page.query_params)
        path_param_combinations = self._get_param_combinations(page.path_params)
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
            urls.append(SiteMapUrl(loc=loc))
        return urls

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
