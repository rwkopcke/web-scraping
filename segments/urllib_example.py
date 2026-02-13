from urllib.request import urlopen

def find_(text, key, term):
    '''
        In 'text',
            find the string that begins immediately
            after 'key' and ends immediately 
            before 'term'
        Using the str.find() method
        Return the string after str.strip()
            to remove any extraneous characters
    '''
    start_idx = text.find(key) + len(key)
    stop_idx = text.find(term, start_idx)
    return text[start_idx : stop_idx].strip()

def find_str(url, key_list, term):
    '''
        Find strings that follow the keys in key_list
        and terminate at term
    '''
    
    page_text = urlopen(url).read().decode('utf-8')
    
    str_list = [
        find_(page_text, key, term)
        for key in key_list
    ]
    
    return str_list