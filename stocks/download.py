import requests

stock_list = []
dls = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
resp = requests.get(dls)
output = open('nasdaq.csv', 'wb')
output.write(resp.content)
output.close()

dls = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download"
resp = requests.get(dls)
output = open('amex.csv', 'wb')
output.write(resp.content)
output.close()

dls = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download"
resp = requests.get(dls)
output = open('nyse.csv', 'wb')
output.write(resp.content)
output.close()

