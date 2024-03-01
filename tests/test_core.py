from sitemapr import Page, Param, SiteMapr, SiteMapUrl


def test_sut_works():
    """System under test should work."""
    # given
    base_url = "https://example.com"
    pages = [
        Page(
            path="",
            query_params=[
                Param(name="page", values=["home", "about", "contact"]),
                Param(name="sort", values=["asc", "desc"]),
            ],
        ),
        Page(
            path="/blog",
            query_params=[
                Param(name="page", values=["1", "2", "3"]),
                Param(name="sort", values=["asc", "desc"]),
            ],
        ),
        Page(
            path="/blog/{id}",
            path_params=[Param(name="id", values=["1", "2", "3"])],
        ),
    ]
    sitemapr = SiteMapr(base_url=base_url, pages=pages)

    # when
    actuals = sitemapr.generate()

    # then
    expected = [
        SiteMapUrl(
            loc="https://example.com?page=home&sort=asc",
            lastmod=None,
            changefreq=None,
            priority=None,
        ),
        SiteMapUrl(
            loc="https://example.com?page=home&sort=desc",
            lastmod=None,
            changefreq=None,
            priority=None,
        ),
        SiteMapUrl(
            loc="https://example.com?page=about&sort=asc",
            lastmod=None,
            changefreq=None,
            priority=None,
        ),
        SiteMapUrl(
            loc="https://example.com?page=about&sort=desc",
            lastmod=None,
            changefreq=None,
            priority=None,
        ),
        SiteMapUrl(
            loc="https://example.com?page=contact&sort=asc",
            lastmod=None,
            changefreq=None,
            priority=None,
        ),
        SiteMapUrl(
            loc="https://example.com?page=contact&sort=desc",
            lastmod=None,
            changefreq=None,
            priority=None,
        ),
        SiteMapUrl(
            loc="https://example.com/blog?page=1&sort=asc",
            lastmod=None,
            changefreq=None,
            priority=None,
        ),
        SiteMapUrl(
            loc="https://example.com/blog?page=1&sort=desc",
            lastmod=None,
            changefreq=None,
            priority=None,
        ),
        SiteMapUrl(
            loc="https://example.com/blog?page=2&sort=asc",
            lastmod=None,
            changefreq=None,
            priority=None,
        ),
        SiteMapUrl(
            loc="https://example.com/blog?page=2&sort=desc",
            lastmod=None,
            changefreq=None,
            priority=None,
        ),
        SiteMapUrl(
            loc="https://example.com/blog?page=3&sort=asc",
            lastmod=None,
            changefreq=None,
            priority=None,
        ),
        SiteMapUrl(
            loc="https://example.com/blog?page=3&sort=desc",
            lastmod=None,
            changefreq=None,
            priority=None,
        ),
        SiteMapUrl(
            loc="https://example.com/blog/1",
            lastmod=None,
            changefreq=None,
            priority=None,
        ),
        SiteMapUrl(
            loc="https://example.com/blog/2",
            lastmod=None,
            changefreq=None,
            priority=None,
        ),
        SiteMapUrl(
            loc="https://example.com/blog/3",
            lastmod=None,
            changefreq=None,
            priority=None,
        ),
    ]
    assert actuals == expected
