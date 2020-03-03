import requests
import json
from pprint import pprint

response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=JE8OJBO4XMZ780PH')

pprint(response.json())
