from collections.abc import Callable
from typing import Literal, TypeVar

from pydantic import BaseModel

T = TypeVar("T")

ChangeFreq = Literal[
    "always", "hourly", "daily", "weekly", "monthly", "yearly", "never"
]

CallbackFn = Callable[[str, dict[str, str], dict[str, str]], T | None]


class Param(BaseModel):
    name: str
    values: list[str] = []


class Page(BaseModel):
    path: str
    query_params: list[Param] = []
    path_params: list[Param] = []
    lastmod: str | None | CallbackFn[str] = None
    changefreq: ChangeFreq | None | CallbackFn[ChangeFreq] = None
    priority: str | None | CallbackFn[str] = None


class SiteMapUrl(BaseModel):
    # Refer to https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=ko#xml
    loc: str
    lastmod: str | None = None
    changefreq: ChangeFreq | None = None  # Google ignores this
    priority: str | None = None  # Google ignores this
