# bookish

`bookish` is a CLI tool for downloading eBooks.

## Demo

```bash
bookish "eloquent javascript"
                                                                                                                                                  
  Title                                                                    Year   Author             Ext     Size   Download                      
 ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
  Eloquent JavaScript: A Modern Introduction to Programming, 3rd Edition   2019   Marijn Haverbeke   epub   18 Mb   https://tinyurl.com/23v4j3wc  
  Eloquent JavaScript: A Modern Introduction to Programming                2019   Marijn Haverbeke   pdf    17 Mb   https://tinyurl.com/26g5csod  
  Eloquent JavaScript: A Modern Introduction to Programming                2019   Marijn Haverbeke   epub   18 Mb   https://tinyurl.com/269ay8hl  
  Eloquent JavaScript: A Modern Introduction to Programming                2019   Haverbeke,Marijn   pdf    17 Mb   https://tinyurl.com/29tftpfe  
  Eloquent Javascript: A Modern Introduction to Programming                2018   Marijn Haverbeke   pdf     3 Mb   https://tinyurl.com/29wypsub
```

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

> [!Important]
> Users are responsible for ensuring their use complies with all applicable laws and regulations.
