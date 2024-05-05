from libgen_api import LibgenSearch
from pyshorteners import Shortener
from rich.console import Console
from rich.table import Table


def search_books(query):
    search = LibgenSearch()
    # results = search.search_title(query)
    filters = {"Language": "English"}
    results = search.search_title_filtered(query, filters)
    return (search, results)


def get_download(search, result):
    resolved = search.resolve_download_links(result)["GET"]
    shortened = Shortener().tinyurl.short(resolved)
    return shortened


def display_results(search, results):
    table = Table(title="Search Results")
    table.add_column("Title", style="magenta", justify="left")
    table.add_column("Year", style="cyan", justify="left")
    table.add_column("Author", style="magenta", justify="left")
    table.add_column("Extension", style="green", justify="left")
    table.add_column("File Size", style="yellow", justify="left")
    table.add_column("Download Link", style="blue", justify="left")

    # Doing this here bc search api doesn't allow more than one extension
    wanted = ("epub", "pdf")
    filtered = [book for book in results if book["Extension"] in wanted]
    for book in filtered:
        # Get resolved download for each search result
        download_link = get_download(search, book)
        table.add_row(
            book["Title"],
            book["Year"],
            book["Author"],
            book["Extension"],
            book["Size"],
            download_link,
        )

    console = Console()
    console.print(table)
