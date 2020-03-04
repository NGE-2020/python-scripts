import requests
from bs4 import BeautifulSoup
from pprint import pprint
import xmltodict

result = requests.get("https://finance.yahoo.com/quote/MCD?p=MCD&.tsrc=fin-srch")

print(result.status_code)

src = result.content

soup = BeautifulSoup(src, 'lxml')
# print(soup.prettify())

# match = soup.title.text
# print(match)

match = soup.find('div', class_='data-reactid')
print(match)
