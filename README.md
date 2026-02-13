# Exercises: Introduction to Web Scraping with Python

Practice
- Parsing website data using string methods and regular expressions
- Parsing website data using an HTML parser
- Interacting with forms and other website components

`uv run main.py`

Demonstrates ways to
- scrape,
- provide authentication, and
- open links
on static web pages

Course:
https://realpython.com/courses/exercises-introduction-web-scraping/
https://realpython.com/beautiful-soup-web-scraper-python/
https://realpython.com/courses/working-json-data-python/

Pages:
- string methods
    - http://olympus.realpython.org/profiles/dionysus
- Beautiful Soup
    - http://olympus.realpython.org/profiles

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
