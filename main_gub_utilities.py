from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup as bs


def get_urllib_read_response(url, hdrs=None):
    '''
        Return urllib response.read() for parsing

    '''
    request = Request(url, headers=hdrs)
    try:
        with urlopen(request, timeout=10) as response:
            print(response.status)
            # Use read() to extract the text from response object
            return response.read(), response
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")
        
        
def decode_and_find(resp_read, resp,
                    tag= None, id= None):
    '''
        Decodes the response.read() obj
        Returns filtered txt obj body
    '''
    character_set = resp.headers.get_content_charset()
    if not character_set:
        character_set = 'utf-8'
    decoded_body = resp_read.decode(character_set)
    
    body_soup = bs(decoded_body, 'html.parser')
    card_grid = body_soup.find(tag, id)
    
    return card_grid


def create_candidate_records(card_grid):
    '''
        find and scrape each candidate's card
        for all cards in card_grid
        
        return a list of records (lists)
        each record contains the pertinent information
        for each candidate
    '''
    # a list of lists (rows)
    candidate_array = list()
    for card in card_grid:
        row = list()
        candidate = card.find('h3').text.strip()
        row.append(candidate)
        
        # load party and statement
        parags = card.find_all('p')
        match len(parags):
            case 0:
                lst = ['', '']
            case 1:
                lst = [parags[0].text.strip(), '']
            case 2:
                lst = [parags[0].text.strip(), 
                    parags[1].text.strip()]
        row.extend(lst)
        
        # load all links as list
        links = [
            link.get('href')
            for link in card.find_all('a')]
        row.append(links)
        
        candidate_array.append(row)
        
    return candidate_array