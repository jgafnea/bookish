from libgen_api import LibgenSearch
from pyshorteners import Shortener
from rich import box
from rich.console import Console
from rich.progress import track
from rich.table import Table


def search_books(query) -> list:

    lang_filter = {"Language": "English"}
    file_filter = ("epub", "pdf")

    search = LibgenSearch()

    filtered = search.search_title_filtered(query, lang_filter)
    results = [book for book in filtered if book["Extension"] in (file_filter)]

    for book in track(results, description="Working..."):

        # Resolve links then shorten so they fit table
        resolved = search.resolve_download_links(book)["GET"]
        tinyurl = Shortener().tinyurl.short(resolved)
        book["Link"] = tinyurl

    return results


def display_results(results):
    # https://rich.readthedocs.io/en/stable/appendix/colors.html
    table = Table(title="", box=box.SIMPLE_HEAD)

    table.add_column("Title", style="bright_cyan")
    table.add_column("Year", style="bright_magenta")
    table.add_column("Author", style="yellow")
    table.add_column("Ext", style="green")
    table.add_column("Size", style="dim", justify="right")
    table.add_column("Download", style="blue")

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
