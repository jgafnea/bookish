import argparse

from libgen_api import LibgenSearch
from pyshorteners import Shortener
from rich.console import Console
from rich.table import Table


def search_books(query):
    search = LibgenSearch()
    results = search.search_title(query)
    return (search, results)


def get_download(search, result):
    resolved = search.resolve_download_links(result)["GET"]
    shortened = Shortener().tinyurl.short(resolved)
    return shortened


def display_results(search, results):
    table = Table(title="Search Results")
    table.add_column("Title", style="cyan", justify="left")
    table.add_column("Author", style="magenta", justify="left")
    table.add_column("Extension", style="green", justify="left")
    table.add_column("File Size", style="yellow", justify="left")
    table.add_column("Download Link", style="blue", justify="left")

    for book in results:
        # Get resolved download for each search result
        download_link = get_download(search, book)
        table.add_row(
            book["Title"],
            book["Author"],
            book["Extension"],
            book["Size"],
            download_link,
        )

    console = Console()
    console.print(table)


def main():
    parser = argparse.ArgumentParser(description="Search books using Libgen API")
    parser.add_argument("query", type=str, help="Search query for books")
    args = parser.parse_args()

    # Passing search around because it's needed to get resolved download links
    search, results = search_books(args.query)

    if results:
        display_results(search, results)
    else:
        console = Console()
        console.print(
            "[bold red]No results found for the query '{}'[/bold red]".format(
                args.query
            )
        )


if __name__ == "__main__":
    main()
