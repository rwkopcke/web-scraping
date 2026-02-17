from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup as bs


def now_string():
    '''
        Used to fetch current date for writing files
    '''
    return datetime.now().strftime("_%m_%d")


def get_urllib_read_response(url, hdrs=None):
    '''
        Return urllib response.read() for parsing
    '''
    request = Request(url, headers=hdrs)
    try:
        with urlopen(request, timeout=20) as response:
            print(response.status)
            # Use read() to extract the text from response object
            return response.read(), response
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")
        
        
def decode_response(resp_read, resp):
    '''
        Decodes the response.read() obj
    '''
    character_set = resp.headers.get_content_charset()
    if not character_set:
        character_set = 'utf-8'
    decoded_body = resp_read.decode(character_set)
    
    return decoded_body


def write_decoded_html(body, 
                       rel_path_to_file,
                       file_extension):
    '''
        Void return
    '''
    file_name = (rel_path_to_file +
                 now_string() + file_extension)
    
    with open(file_name, 'w') as to_file:
        to_file.write(body)
        
        
def read_decoded_html_file(dir, file_ext):
    '''
        Read stored decoded html
        files in list are strings that
            include relative path 
    '''
    files = [str(f) 
             for f in Path(dir).glob("*" + file_ext)]
            
    match len(files):
        case 0:
            print(f'\n{dir} has no {file_ext} files\n')
            quit()
        case 1:
            read_file = files[0]
        case _:
            read_file = max(sorted(files))[0]
    
    with open(read_file, 'r') as from_file:
        decoded_html = from_file.read()
        
    return decoded_html
    
    
def filter_html(decoded_body, tag= None, id= None):
    '''
        Filters decoded_html to isolate block of html
    '''
    body_soup = bs(decoded_body, 'html.parser')
    card_grid = body_soup.find(tag, id)
    
    return card_grid


def create_candidate_records(card_grid,
                             name_tag,
                             party_tag,
                             party_class,
                             web_tag,
                             web_ref):
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
        candidate = card.find(name_tag).text.strip()
        row.append(candidate)
        
        # load party and statement
        parags = card.find_all(party_tag)
        match len(parags):
            case 0:
                lst = ['', '']
            case 1:
                if party_class in parags[0]['class'][0]['class'][0]:
                    lst_0 = parags[0].text.strip()
                else:
                    lst_0 = ''
                    lst_1 = parags[1].text.strip()
            case 2:
                lst_0 = parags[0].text.strip()
                lst_1 = parags[1].text.strip()
        row.extend([lst_0, lst_1])
        
        # load all links as list
        links = [
            link.get(web_ref)
            for link in card.find_all(web_tag)]
        row.append(links)
        
        candidate_array.append(row)
        
    return candidate_array


def save_candidates(df, 
                    rel_path_to_file, 
                    file_ext):
    '''
        
    '''
    file_addr = rel_path_to_file + now_string() + file_ext
    with open(file_addr, 'w') as to_file:
        df.write_parquet(to_file)
    
    return