import requests
from bs4 import BeautifulSoup

ticker = 'BRMK.WS'
url = 'https://finance.yahoo.com/quote/{st}'.format(st=ticker)
res = requests.get( url )
html = res.text

soup = BeautifulSoup( html, 'html.parser' )

test = str(soup)
# try:
#     market_cap_elem = soup.find( 'td', { 'data-test' : 'ONE_YEAR_TARGET_PRICE-value' } )
#
# finally:
#     market_cap = market_cap_elem.text

if "ONE_YEAR_TARGET_PRICE-value" in test:
    print("esta al pedo")
else:
    print("no vale pito")

# print(market_cap_elem)

# def respuesta():
#     response = requests.get('https://finance.yahoo.com/quote/BWL.A')
#     html = response.text
#     if len(html) > 0:
#         return html
#     else:
#         return None
#
# print(respuesta())
