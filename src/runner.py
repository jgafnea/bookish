import argparse
import sys

from rich.console import Console

from .search import display_results, search_books


# def run():
def main():
    parser = argparse.ArgumentParser(description="Search books using Libgen API")
    parser.add_argument("query", type=str, help="Search query for books")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    results = search_books(args.query)

    if results:
        display_results(results)
    else:
        console = Console()
        console.print(
            "[bold red]No results found for the query '{}'[/bold red]".format(
                args.query
            )
        )


if __name__ == "__main__":
    main()
