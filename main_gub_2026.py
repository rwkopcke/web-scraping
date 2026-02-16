import polars as pl

import main_gub_utilities as ut


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++  parameters

url = 'https://mainemorningstar.com/race-details/2026-gubernatorial-election/'
 # Full URL to get the content from google cache
url_full = 'https://webcache.googleusercontent.com/search?q=cache:' + url
# The headers to for requests.get 
hdrs = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'}

# The headers for the scraped content
headers = [
    'candidate',
    'party',
    'statement',
    'websites']

# full set of candidates' cards (the grid)
tag = 'div'
id = "electionRaceCandidateGrid"

# candidates' details
candidate_details = {
    'name_tag': 'h3',
    'party_tag': 'p',
    'party_class': "Title",
    'web_tag': 'a',
    'web_ref': 'href'
}

io_dir = 'io_gub'
rel_path_decoded_html = io_dir + '/' + 'main_gub_2026'
file_ext_decoded_html = '.html'
rel_path_data = io_dir + '/' + 'main_gub_df_2026'
file_ext_data = '.parquet'

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++  scrape and parse the url

scrape = input('Scrape again, or read stored data?\n' +
               'Enter yes or no: ')

if scrape in ['yes', 'Yes', 'YES', 'y', 'Y']:
    
    # scrape new data
    resp_read, resp = ut.get_urllib_read_response(url, hdrs= hdrs)
    decoded_html = ut.decode_response(resp_read, resp)
    # save
    ut.write_decoded_html(decoded_html,
                        rel_path_decoded_html,
                        file_ext_decoded_html)

else:
    # read decoded_html from file
    decoded_html = \
        ut.read_decoded_html_file(io_dir, file_ext_decoded_html)

# isolate candidate grid, then find list of names in grid
candidate_names_lst = \
    ut.filter_html(decoded_html, tag, id).find_all('h3')

# create a generator of candidates' cards from their "names"
candidate_cards = (
    item.parent.parent for item in candidate_names_lst)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++  scrape each card for information
# +++++  create & save candidate X candidate details array

candidate_array = ut.create_candidate_records(
                        candidate_cards,
                        **candidate_details)

candidate_df = pl.DataFrame(candidate_array,
                            schema = headers,
                            orient= 'row')
print(candidate_df)

ut.save_candidates(candidate_df,
                   rel_path_data,
                   file_ext_data)
