## bookish

`bookish` is a CLI tool for downloading eBooks.

### Example

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

### Usage

Requires [Docker](https://docs.docker.com/get-docker/) or [Poetry](https://python-poetry.org).

 #### Docker

```bash
git clone https://github.com/jgafnea/bookish && cd bookish
docker build -t bookish .

# Using with optional alias:
alias bookish="docker run --rm -it bookish"
bookish "book title"

# Using without alias:
docker run --rm -it bookish "book title"
```

#### Poetry

```bash
git clone https://github.com/jgafnea/bookish && cd bookish
poetry install

# Using with optional alias:
alias bookish="poetry run bookish"
bookish "book title"
```

> [!IMPORTANT]
> Tool is meant for legal use only. Piracy is bad, mmm kay?
