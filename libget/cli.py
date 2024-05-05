import argparse

from rich.console import Console

from .search import display_results, search_books


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
