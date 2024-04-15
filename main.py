import argparse

from libgen_api import LibgenSearch
from rich.console import Console
from rich.table import Table


# def search_books(query, count=10):
def search_books(query):
    search = LibgenSearch()
    results = search.search_title(query)
    return results


def display_results(results):
    table = Table(title="Search Results")
    table.add_column("Title", style="cyan", justify="left")
    table.add_column("Author", style="magenta", justify="left")
    table.add_column("Extension", style="green", justify="left")
    table.add_column("File Size", style="yellow", justify="left")
    table.add_column("Download Link", style="blue", justify="left")

    for book in results:
        table.add_row(
            book["Title"],
            book["Author"],
            book["Extension"],
            book["Size"],
            book["Mirror_1"],
        )

    console = Console()
    console.print(table)


def main():
    # console = Console()
    parser = argparse.ArgumentParser(description="Search books using Libgen API")
    parser.add_argument("query", type=str, help="Search query for books")
    args = parser.parse_args()

    # query = Prompt.ask("Enter your search query:")
    # count = Prompt.ask(
    #     "Enter the number of results to display:", default="10", type=int
    # )
    # parser =
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
