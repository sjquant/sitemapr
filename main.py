from pprint import pprint

from sitemapr import Page, Param, SiteMapr

sm = SiteMapr(
    base_url="https://example.com",
    pages=[
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
    ],
)

pprint(sm.generate())
