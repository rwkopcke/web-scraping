import mechanicalsoup as ms

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
    'home website',
    'star website']

# full set of candidates' cards (the grid)
tag = 'div'
id = "electionRaceCandidateGrid"

# card ids
card_tag = 'div'
card_class = "electionRaceCandidateCardContainer col-12 col-sm-6 col-lg-9 col-xl-6 mb-5"

# candidates' details
name_tag = 'h3'
party_tag = 'p' 
party_class = "electionRaceCandidateTitle mb-3"
stmnt_tag = 'p'
stmnt_class = "electionCandidateBlurb mb-0"
web_tag = 'a'
web_tag_href = 'href'


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++  scrape and parse the url

resp_read, resp = ut.get_urllib_read_response(url, hdrs= hdrs)

# find the grid of candidates' cards
candidates_grid = ut.decode_and_find(resp_read, resp, tag, id)

# crawl through the card grid, fetching candidates' names (22)
candidate_names_lst = candidates_grid.find_all('h3')

# create a generator of candidates' cards from their names
candidate_cards = (
    item.parent.parent for item in candidate_names_lst
)

candidate_array = \
    ut.create_candidate_records(candidate_cards)
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++  scrape each card for intormation


