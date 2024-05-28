from collections import namedtuple

from libgen_api import LibgenSearch
from pyshorteners import Shortener
from rich.progress import Progress

Book = namedtuple("Book", "title, year, author, extension, size, download")
books = []


def search(query) -> list:

    search = LibgenSearch()

    lang_filter = {"Language": "English"}
    file_filter = ("epub", "pdf")

    # Filter twice, first using libgen for language, then using our own for file type.
    results = search.search_title_filtered(query, lang_filter)
    results = [r for r in results if r["Extension"] in (file_filter)]

    with Progress(transient=True) as progress:
        # Use len(results) for "work" so progress updates correctly.
        total_work = len(results)
        task = progress.add_task("Working…", total=total_work)

        for book_data in results:
            # Resolve download link from mirror.
            resolved = search.resolve_download_links(book_data)["GET"]
            tinyurl = Shortener().tinyurl.short(resolved)
            book_data["Download"] = tinyurl

            book_map = {
                # Make keys lowercase.
                key.lower(): value
                for key, value in book_data.items()
                # Limit keys from dict using keys from Book.
                if key.lower() in set(Book._fields)
            }

            # Create new Book objects and add to list.
            book = Book(**book_map)
            books.append(book)

            # Update progress after each book.
            progress.update(task, advance=1)

    # Sort list so rich table shows most-recent first.
    books.sort(key=lambda book: book.year, reverse=True)

    return books
