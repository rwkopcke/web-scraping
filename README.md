# Introduction to Web Scraping with Python
version = "Feb 14, 2026"

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

## II. Project: Scrape Web for Gubernatorial Race in ME 2026
### `uv run main_gub_2026.py`

https://mainemorningstar.com/race-details/2026-gubernatorial-election/

<br></br>

## III. References for Real Python learning path

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

Also:
```
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_cards = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_card in python_job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    link_url = job_card.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")
```
