import requests
import csv
from bs4 import BeautifulSoup
from pprint import pprint
import yfinance as yf

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

    res = requests.get( url )
    html = res.text

    soup = BeautifulSoup( html, 'html.parser' )
    test = str(soup)
    if "ONE_YEAR_TARGET_PRICE-value" in test:
        market_cap_elem = soup.find( 'td', { 'data-test' : 'ONE_YEAR_TARGET_PRICE-value' } )
        market_cap = market_cap_elem.text
        return(market_cap)
    else:
        return('false')

def stock_today(stock):
    ticker = stock
    try:
        msft = yf.Ticker(stock)
        print(msft)
        stock_last_close = msft.info['previousClose']
        return(stock_last_close)
    except IndexError as shit:
        print("valip pito")
        pass
    except ValueError as shit:
        print("valip pito")
        pass
    except AttributeError as shit:
        print("valip pito")
        pass

def top20_1y_premonition_from_yahoo(all_stocks):
    huge_top_20 = []
    nine_times_top_20 = []
    eight_times_top_20 = []
    seven_times_top_20 = []
    six_times_top_20 = []
    five_times_top_20 = []
    four_times_top_20 = []
    tree_times_top_20 = []
    two_times_top_20 = []

    for stock in all_stocks:
        one_y_premonition = one_y_premonition_yahoo(stock)
        print(stock, "and",one_y_premonition)
        # stock_price = stock_today(stock)

        # times_grow = float(one_y_premonition) / float(stock_price)
        # print(stock_price, " and", stock)
    #
    #     if times_grow >= 2.0 and times_grow < 3.0:
    #         two_times_top_20.append(stok)
    #     elif times_grow >= 3.0 and times_grow < 4.0:
    #         tree_times_top_20.append(stok)
    #     elif times_grow >= 4.0 and times_grow < 5.0:
    #         four_times_top_20.append(stok)
    #     elif times_grow >= 5.0 and times_grow < 6.0:
    #         five_times_top_20.append(stok)
    #     elif times_grow >= 6.0 and times_grow < 7.0:
    #         six_times_top_20.append(stok)
    #     elif times_grow >= 7.0 and times_grow < 8.0:
    #         seven_times_top_20.append(stok)
    #     elif times_grow >= 8.0 and times_grow < 9.0:
    #         eight_times_top_20.append(stok)
    #     elif times_grow >= 9.0 and times_grow < 10.0:
    #         nine_times_top_20.append(stok)
    #     else:
    #         huge_top_20.append(stok)
    #
    # top20_list = [ten_times_top_20, nine_times_top_20, eight_times_top_20, seven_times_top_20, six_times_top_20, five_times_top_20, four_times_top_20, tree_times_top_20, two_times_top_20]
    #
    # return(top20_list)


def main():

    all_stocks = get_stock_list()

    top20_list = top20_1y_premonition_from_yahoo(all_stocks)

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
