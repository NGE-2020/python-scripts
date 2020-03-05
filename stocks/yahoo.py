import requests
import csv
from bs4 import BeautifulSoup
from pprint import pprint
import yfinance as yf
import threading

def get_stock_list():
    stocks = {'APPL'}

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

    with open('amex.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
                stocks.add(row[0])

    with open('nasdaq.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                    stocks.add(row[0])

    with open('nyse.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                    stocks.add(row[0])
    return(stocks)

def one_y_premonition_yahoo(stock):
    ticker = stock
    url = 'https://finance.yahoo.com/quote/' + ticker

    premo = ''
    actual = ''

    res = requests.get( url )
    html = res.text
    soup = BeautifulSoup( html, 'html.parser' )
    test = str(soup)
    if "ONE_YEAR_TARGET_PRICE-value" in test:
        premo_elem = soup.find( 'td', { 'data-test' : 'ONE_YEAR_TARGET_PRICE-value' } )
        premo = premo_elem.text
        premo = premo.replace(',','')
        premo = premo.replace('$','')

        actual_elem = soup.find( 'span', { 'class' : 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)' } )
        actual = actual_elem.text
    else:
        return('false')

    print(premo)
    print(actual)

# def top20_threaths(stock):
#     huge_stock = []
#
#     one_y_premonition = one_y_premonition_yahoo(stock)
#     stock_price = stock_today_ameritrade(stock)
#     if "false" in one_y_premonition:
#         pass
#     elif "N/A" in one_y_premonition:
#         pass
#     else:
#         if 'false' in stock_price:
#             pass
#         else:
#             times_grow = float(one_y_premonition) / float(stock_price)
#             if times_grow > 2.0:
#                 print("The premonition for the stock ", stock, "is more than twice")
#
# def threaths(all_stocks, function):
#     threaths = []
#
#     for stock in all_stocks:
#         try:
#             th = threading.Thread(target=function, args=(stock))
#             th.start()
#
#         finally:
#             threaths.append(th)
#
#     for tr in threaths:
#         tr.join()

def main():
    all_stocks = get_stock_list()
    print(all_stocks)
    for stock in all_stocks:
        print(stock)
        data = top20_1y_premonition_from_yahoo(stock)
        print(data)
