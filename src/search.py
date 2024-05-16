from libgen_api import LibgenSearch
from pyshorteners import Shortener
from rich import box
from rich.console import Console
from rich.progress import Progress
from rich.table import Table


def search_books(query) -> list:

    lang_filter = {"Language": "English"}
    file_filter = ("epub", "pdf")

    search = LibgenSearch()

    # Filter twice, first using libgen for language, then using our own for file type.
    pending = search.search_title_filtered(query, lang_filter)
    results = [book for book in pending if book["Extension"] in (file_filter)]

    # Capture length so progress advances correctly.
    total_work = len(results)

    with Progress(transient=True) as progress:
        task = progress.add_task("Working...", total=total_work)

        for book in results:

            resolved = search.resolve_download_links(book)["GET"]
            tinyurl = Shortener().tinyurl.short(resolved)
            book["Link"] = tinyurl

            progress.update(task, advance=1)

    return results


def display_results(results) -> None:
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
