from urllib.request import urlopen
from requests import get as req_get

from bs4 import BeautifulSoup as bs
import mechanicalsoup as ms

def find_links(url, base_url):
    '''
        Finds links in url
    '''
    page_text = urlopen(url).read().decode('utf-8')
    
    soup = bs(page_text, features= 'html.parser')
    
    links_list = [
        base_url + link['href'].strip()
        for link in soup.find_all('a')
    ]
    
    return links_list


def find_card_info(url):
    '''
    To scrape "cards" in a web site that have 'python' in their h2:
    First, find the eligible cards that contain python deeply
        nested in their information (find_all returns a list)
    Then, build a list of all eligible cards, by selecting the 
        entire card in the find_all list using .parent
    
    python_jobs = \
        soup.find_all("h2", 
                      string=lambda text: "python" in text.lower())
                         
    Fetches the text of each <h2> element, converts it to lowercase, 
        and checks if the substring "python" is found anywhere.
    
    python_job_cards = [
        h2_element.parent.parent.parent for h2_element in python_jobs]
        
    To select the parent element of the parent element of the parent element 
        of each <h2> title element that contains 'python'.
    '''

    page = req_get(url)  #requests.get(url)

    soup = bs(page.content, "html.parser")
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
        print()
        
    return

def browser_actions(login_url):
    '''
    '''
    browser = ms.StatefulBrowser()
    browser.open(login_url)
    # line below shows <Response [200]> & requests object
    #print(browser.open(login_url),
    #      type(browser.open(login_url)))
    print(browser.url)
    # .page is a bs4.BeautifulSoup object
    #print(browser.page, type(browser.page))
    
    # find the form and 
    # the following complete the form's named fields
    browser.select_form('form')
    browser['user'] = 'zeus'
    browser['pwd'] = 'ThunderDude'
    # shows <Response [200]>
    # print(browser.submit_selected())
    browser.submit_selected()
    # shows that browser has moved to the next page
    print(browser.page.title)
    print(browser.page)
    
    return