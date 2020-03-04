import requests
from bs4 import BeautifulSoup

ticker = 'AAPL'
url = 'https://finance.yahoo.com/quote/' + ticker

res = requests.get( url )
html = res.text

soup = BeautifulSoup( html, 'html.parser' )
market_cap_elem = soup.find( 'td', { 'data-test' : 'ONE_YEAR_TARGET_PRICE-value' } )
market_cap = market_cap_elem.text

print(market_cap)
