# Introduction to Web Scraping with Python
version: "February 23, 2026"

<br></br>

## I. Examples and Exercises
### `uv run main.py`

Practice
- Parsing website data using string methods, urllib
- Parsing website data using BeautifulSoup4
- Interacting with forms using MechanicalSoup

Demonstrates ways to
- scrape,
- provide authentication, and
- open links
on static web pages

<br></br>

## II. Scrape Web for Gubernatorial Race in ME 2026
### `uv run main_gub_2026.py`

https://mainemorningstar.com/race-details/2026-gubernatorial-election/

<br></br>

## III. Structure of Project

```
web-scraping % tree
.
├── io_gub
│   ├── main_gub_2026_02_23.html
│   ├── main_gub_df_2026_02_23.csv
│   ├── main_gub_df_2026_02_23.parquet
│   └── main_gub_df_2026_02_23.txt
├── io_main
│   ├── complex_data.json
│   ├── employee_birthday.txt
│   ├── employee_file_dict.csv
│   ├── employee_file.csv
│   └── filtered_data_file.json
├── main_gub_2026.py
├── main_gub_utilities.py
├── main.py
├── pyproject.toml
├── README.md
├── segments
│   ├── __init__.py
│   ├── bs4_example.py
│   ├── csv_example.py
│   ├── json_example.py
│   └── urllib_example.py
└── uv.lock

% uv tree
web-scraping v23.2.2026
├── beautifulsoup4 v4.14.3
│   ├── soupsieve v2.8.3
│   └── typing-extensions v4.15.0
├── bs4 v0.0.2
│   └── beautifulsoup4 v4.14.3 (*)
└── polars v1.38.1
    └── polars-runtime-32 v1.38.1
(*) Package tree already displayed

```

<br></br>

## IV. References for Real Python learning path and Notes

Course:
https://realpython.com/courses/exercises-introduction-web-scraping/
https://realpython.com/beautiful-soup-web-scraper-python/
https://realpython.com/courses/working-json-data-python/

Pages:
- string methods
    - http://olympus.realpython.org/profiles/dionysus
- Beautiful Soup
    - http://olympus.realpython.org/profiles

https://realpython.com/urllib-request/
https://docs.python.org/3/howto/urllib2.html
https://www.scrapehero.com/scraping-with-python-urllib/
https://scrapeops.io/python-web-scraping-playbook/python-beautifulsoup-find/
