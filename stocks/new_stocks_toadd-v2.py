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

def one_y_premonition_yahoo(stock, premo_dic):

    premo = premo_dic

    ticker = stock
    url = 'https://finance.yahoo.com/quote/' + ticker

    res = requests.get( url )
    html = res.text

    soup = BeautifulSoup( html, 'html.parser' )
    test = str(soup)
    if "ONE_YEAR_TARGET_PRICE-value" in test:
        market_cap_elem = soup.find( 'td', { 'data-test' : 'ONE_YEAR_TARGET_PRICE-value' } )
        market_cap = market_cap_elem.text
        market_cap = market_cap.replace(',','')
        market_cap = market_cap.replace('$','')
        premo.update({stock:{'premo':market_cap}})
    else:
        premo.update({stock:{'premo':'false'}})

    print(premo)
    return(premo)

def premonition_threaths(all_stocks, premo_dic, function):
    threaths = []

    for stock in all_stocks:
        try:
            th = threading.Thread(target=function, args=(stock, premo_dic))
            th.start()

        finally:
            threaths.append(th)

    for tr in threaths:
        tr.join()

def stock_today_ameritrade(stock):
    ticker = stock

    url = 'https://www.tdameritrade.com/search/results.page?q=' + ticker

    res = requests.get( url )
    html = res.text

    soup = BeautifulSoup( html, 'html.parser' )
    test = str(soup)
    if "current-stock-price" in test:
        market_cap_elem = soup.find('span',{'class' : 'current-stock-price'})
        market_cap = market_cap_elem.text
        market_cap = market_cap.replace(',','')
        market_cap = market_cap.replace('$','')
        return(market_cap)
    else:
        return('false')

def actual_threaths(all_stocks, premo_dic, function):
    threaths = []

    for stock in all_stocks:
        try:
            th = threading.Thread(target=function, args=(stock, premo_dic))
            th.start()

        finally:
            threaths.append(th)

    for tr in threaths:
        tr.join()

def get_stock_data(all_stocks):
    stock_dic = {}
    for stock in all_stocks:
        one_y_premonition = one_y_premonition_yahoo(stock)
        stock_price = stock_today_ameritrade(stock)
        if "false" in one_y_premonition:
            pass
        elif "N/A" in one_y_premonition:
            pass
        else:
            if 'false' in stock_price:
                pass
            else:
                stock_dic.update({stock:{'premo':one_y_premonition}})
                stock_dic[stock].update({'actual':stock_price})
                pprint(stock_dic)
                times_grow = float(one_y_premonition) / float(stock_price)
                if times_grow > 2.0:
                    print("The premonition for the stock", stock, "is more than twice")

def main():

    all_stocks = get_stock_list()

    # top20_list = get_stock_data(all_stocks)

    dic = {}

    premo_dic = premonition_threaths(all_stocks, dic, one_y_premonition_yahoo)

    stock_dic = actual_threaths(all_stocks, premo_dic, stock_today_ameritrade)

    # for stock in top20_list:
    #     """
    #     Ver
    #         Cuanto tiempo tiene la empresa
    #         Cuanta es su ganancia en el ultimo anio y mes
    #         Entender lo de el volumen para cuantificarlo
    #         Ver los stackeholders
    #         obtener el website
    #         Numero de empleados
    #         numero de shares 'floatShares"
    #          'fiftyDayAverage': 173.32559,
    #          'fiftyTwoWeekHigh': 190.7,
    #          'fiftyTwoWeekLow': 108.8,
    #         'enterpriseValue'
    #          'enterpriseToEbitda': 19.345,
    #          'enterpriseToRevenue': 8.828,
    #          'earningsQuarterlyGrowth': 0.383,
    #          'averageDailyVolume10Day': 75622200,
    #          'averageVolume': 31802203,
    #          'averageVolume10days': 75622200,
    #     """
    #     append values in an ordered way to top20_table
    #
    # print(top20_table) """ As a pretty table """

if __name__ == '__main__':
    main()
