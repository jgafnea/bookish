# bookish

`bookish` is a CLI tool for downloading eBooks.


## Usage

Install and run using [Docker](https://docs.docker.com/get-docker/) or [Poetry](https://python-poetry.org):

 
### Docker

```bash
git clone https://github.com/jgafnea/bookish && cd bookish
docker build -t bookish .
docker run --rm -it bookish "BOOK TITLE"

# OPTIONAL: Use alias
alias bookish="docker run --rm -it bookish"
bookish "BOOK TITLE"
```

### Poetry

```bash
git clone https://github.com/jgafnea/bookish && cd bookish
poetry install
poetry run bookish "BOOK TITLE"

# OPTIONAL: Use alias
alias bookish="poetry run bookish"
bookish "BOOK TITLE"
```

> [!Warning]
> Users are responsible for ensuring their use of this tool complies with all applicable laws and regulations.
