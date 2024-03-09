import pathlib

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
    actuals = list(sitemapr.iter_urls())

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


def test_save(tmp_path: pathlib.Path):
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
    save_path = tmp_path / "sitemap.xml"
    sitemapr.save(str(save_path))

    # then
    with open(save_path) as f:
        content = f.read()
        assert (
            content
            == '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://example.com?page=home&sort=asc</loc></url><url><loc>https://example.com?page=home&sort=desc</loc></url><url><loc>https://example.com?page=about&sort=asc</loc></url><url><loc>https://example.com?page=about&sort=desc</loc></url><url><loc>https://example.com?page=contact&sort=asc</loc></url><url><loc>https://example.com?page=contact&sort=desc</loc></url><url><loc>https://example.com/blog?page=1&sort=asc</loc></url><url><loc>https://example.com/blog?page=1&sort=desc</loc></url><url><loc>https://example.com/blog?page=2&sort=asc</loc></url><url><loc>https://example.com/blog?page=2&sort=desc</loc></url><url><loc>https://example.com/blog?page=3&sort=asc</loc></url><url><loc>https://example.com/blog?page=3&sort=desc</loc></url><url><loc>https://example.com/blog/1</loc></url><url><loc>https://example.com/blog/2</loc></url><url><loc>https://example.com/blog/3</loc></url></urlset>'
        )
