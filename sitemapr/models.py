from typing import Literal

from pydantic import BaseModel

ChangeFreq = Literal[
    "always", "hourly", "daily", "weekly", "monthly", "yearly", "never"
]


class Param(BaseModel):
    name: str
    values: list[str] = []


class Page(BaseModel):
    path: str
    query_params: list[Param] = []
    path_params: list[Param] = []
    lastmod: str | None = None
    changefreq: ChangeFreq | None = None
    priority: float | None = None


class SiteMapUrl(BaseModel):
    # Refer to https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=ko#xml
    loc: str
    lastmod: str | None = None
    changefreq: ChangeFreq | None = None  # Google ignores this
    priority: float | None = None  # Google ignores this
