from segments import urllib_example as urllib_ex
from segments import bs4_example as b_soup
from segments import json_example as json_ex
from segments import csv_example as csv_ex


def main():
    '''
        Demonstrate ways 
            to scrape,
            to provide authentication, and
            to open links
        on static web pages
    '''
    print("Hello from web-scraping!\n")
    
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++  scrape using urllib and string methods
# +++++  find name and favorite color
    
    url = 'http://olympus.realpython.org/profiles/dionysus'
    Key_list = ['Name: ', 'Favorite Color: ']
    
    results_list = urllib_ex.find_str(url, Key_list, '<')

    print(results_list)
    print()
    
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++  get links using Beautiful Soup
# +++++  find http links for the names on the page

    
    base_url = 'http://olympus.realpython.org'
    url = base_url + '/profiles'
    
    links_list = b_soup.find_links(url, base_url)
    print(links_list)
    print()
    
    # a more complicated example
    url = "https://realpython.github.io/fake-jobs/"
    
    b_soup.find_card_info(url)
    print()
        
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++  interact with html forms, fill forms
# +++++  click for redirects

    base_url = 'http://olympus.realpython.org'
    login_url = base_url + '/login'
    
    b_soup.browser_actions(login_url)
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++  JSON 
# +++++  receiving and working with json objects in python

    url = 'https://jsonplaceholder.typicode.com/todos'
    
    json_ex.json_response(url)
    print()
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++  JSON 
# +++++  receiving and working with json objects in python

    json_ex.json_custom_obj()
    print()
    
    json_ex.json_custom_encoder()
    print()
    
    json_ex.json_decode_custom_types()
    print()
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++  CSV
# +++++  receiving and working with json objects in python    

    csv_file = csv_ex.read_csv_file()
    print()
    
    csv_ex.write_csv_file(csv_file)
    print()
    
    csv_file, header_list = csv_ex.read_csv_file_2()
    print()
    
    csv_ex.write_csv_file_2(csv_file, header_list)
    print()
    

if __name__ == "__main__":
    main()