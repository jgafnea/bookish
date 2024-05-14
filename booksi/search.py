from libgen_api import LibgenSearch
from pyshorteners import Shortener
from rich.console import Console
from rich.table import Table


def search_books(query) -> list:

    lang_filter = {"Language": "English"}
    file_filter = ("epub", "pdf")

    search = LibgenSearch()

    filtered = search.search_title_filtered(query, lang_filter)
    results = [book for book in filtered if book["Extension"] in (file_filter)]

    for book in results:
        # Resolve links then shorten so they fit table
        resolved = search.resolve_download_links(book)["GET"]
        tinyurl = Shortener().tinyurl.short(resolved)
        book["Link"] = tinyurl

    return results


def display_results(results):
    # https://rich.readthedocs.io/en/stable/appendix/colors.html
    table = Table(title="Search Results")
    table.add_column("Title", style="bright_cyan", justify="left")
    table.add_column("Year", style="cyan", justify="left")
    table.add_column("Author", style="bright_magenta", justify="left")
    table.add_column("Ext", style="green", justify="left")
    table.add_column("Size", style="bright_green", justify="right")
    table.add_column("Link", style="bright_blue", justify="left")

    for book in results:
        table.add_row(
            book["Title"],
            book["Year"],
            book["Author"],
            book["Extension"],
            book["Size"],
            book["Link"],
        )

    console = Console()
    console.print(table)
