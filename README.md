# sitemapr

`sitemapr` is a Python library designed to generate and save sitemaps for websites. It allows for the creation of detailed sitemaps with customizable parameters, making it easier for search engines to crawl and index web pages efficiently.

## Features

- Generate sitemaps with dynamic URL parameters.
- Split large sitemaps into chunks to comply with sitemap index specifications.
- Customizable base URLs for sitemaps and websites.

## Installation

SiteMapr can be easily installed using pip. Ensure you have pip installed and run the following command:

```sh
pip install sitemapr
```

This command will download and install SiteMapr along with its dependencies.

## Quick Start

Here's how to quickly generate a sitemap for your website using SiteMapr:

1. **Define Your Pages**: First, define the pages you want to include in your sitemap, including any dynamic path or query parameters.

2. **Create a SiteMapr Instance**: Initialize SiteMapr with your website's base URL and the pages you've defined.

3. **Save Your Sitemap**: Choose a directory and save your sitemap, specifying chunk sizes if needed.

### Example

```python
from sitemapr import Page, Param, SiteMapr

# Define the pages of your site
pages = [
    Page(
        path="",
        query_params=[
            Param(name="page", values=["home", "about", "contact"]),
            Param(name="sort", values=["asc", "desc"]),
        ],
        priority="1.0",
    ),
    Page(
        path="/blog",
        query_params=[
            Param(name="page", values=["1", "2", "3"]),
            Param(name="sort", values=["asc", "desc"]),
        ],
        # For lastmod, priority, and changefreq field, you can use callback function for more precise control
        lastmod=lambda loc, path_params, query_params: "2024-05-07T00:00:00+00"
    ),
    Page(
        path="/blog/{id}",
        path_params=[Param(name="id", values=["1", "2", "3"])],
    ),
]

# Initialize SiteMapr with your website's base URL and the defined pages
sitemapr = SiteMapr(base_url="https://example.com", pages=pages)

# Save the sitemap to the specified directory
sitemapr.save("/path/to/your/sitemap/directory")
```

## License

`sitemapr` is released under the MIT License. See the LICENSE file for more details.
