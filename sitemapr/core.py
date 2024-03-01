from typing import Literal

from pydantic import BaseModel

Source = Literal["sql", "values"]


class Param(BaseModel):
    name: str
    source: Source = "values"
    query: str | None = None
    values: list[str] | None = None


class Page(BaseModel):
    path: str
    query_params: list[Param] | None = None
    path_params: list[Param] | None = None


class SiteMapr:
    def __init__(self, base_url: str, pages: list[Page]):
        self._base_url = base_url
        self._pages = pages

    def generate(
        self,
        *,
        outdir: str = ".",
        filename: str = "sitemap.xml",
        limit_per_file: int = 50000
    ):
        print("Generating sitemap...")
