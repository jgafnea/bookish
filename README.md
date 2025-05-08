
# bookish

![Tests](https://github.com/jgafnea/bookish/actions/workflows/python.yml/badge.svg)

<img src="./assets/example.png" alt="Command output example" style="max-width: 80%; height: auto;">

`bookish` is a CLI tool created to search and download eBooks without navigating spammy websites.

## Usage

Use Docker or Poetry:

### Docker

```bash
git clone https://github.com/jgafnea/bookish && cd bookish
docker build -t bookish .

# Using with optional alias:
alias bookish="docker run --rm -it bookish"
bookish "eloquent javascript"

# Using without alias:
docker run --rm -it bookish "eloquent javascript"
```

### Poetry

```bash
git clone https://github.com/jgafnea/bookish && cd bookish
poetry install

# Using with optional alias:
alias bookish="poetry run bookish"
bookish "eloquent javascript"

# Using without alias:
poetry run bookish "eloquent javascript"
```
