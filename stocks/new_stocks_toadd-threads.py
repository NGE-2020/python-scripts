import requests
import csv
import json
from bs4 import BeautifulSoup
from pprint import pprint
import yfinance as yf
import threading

def get_stock_list():
    stocks = []
    with open('stock_data.txt') as stock_string:
        stocks = stock_string.read()
        stocks = stocks.split(',')

    clean_data = []
    for stock in stocks:
        if "^" in stock:
            stock = stock.replace("^", "-")
            clean_data.append(stock)
        elif "." in stocks:
            stock = stock.replace(".", "-")
            clean_data.append(stock)
        else:
            clean_data.append(stock)

    clean_data = clean_data[:10]
    print("Will work with ", len(clean_data), "stocks\n")
    return(clean_data)

def grow_measurement(stock, percetage):
    interesting_data = {}
    try:
        info = yf.Ticker(stock)
        oney_hist = info.history(period="1y")
        oney_hist_string = str(oney_hist)
        oney_hist_list1 = oney_hist_string.split('\n')
        oney_hist_list2 = oney_hist_list1[2].split(' ')
        last_year =  float(oney_hist_list2[4])

        stock_last_close = info.info['previousClose']

        anual_grow = ((stock_last_close*100)/last_year) - 100
        anual_grow = round(anual_grow, 2)
        if anual_grow >= float(percetage):
            interesting_data.update({stock:{'anual_grow':anual_grow}})
            interesting_data[stock].update({'actual':stock_last_close})

    except IndexError:
        # print('valio pito')
        pass
    except ValueError:
        # print('valio mas pito')
        pass
    except ImportError:
        # print('valio mucho mas pito')
        pass
    except urllib.error.HTTPError:
        # print('valio mucho mas pito')
        pass

    with open("stock_data.json", "r+") as file:
        data = json.load(file)
        data.update(interesting_data)
        file.seek(0)
        json.dump(data, file)

def grow_threaths(all_stocks, percetage, function):
    threaths = []

    for stock in all_stocks:
        try:
            th = threading.Thread(target=function, args=(stock, percetage))
            th.start()

        finally:
            threaths.append(th)

    for tr in threaths:
        tr.join()

def one_y_premonition_yahoo():
    interesting_data = {}

    with open("stock_data.json", 'r') as outfile:
        interesting_data = json.loads(outfile.read())

    for key,value in interesting_data.items():
        url = 'https://finance.yahoo.com/quote/' + key
        res = requests.get( url )
        html = res.text
        soup = BeautifulSoup( html, 'html.parser' )
        test = str(soup)
        if "ONE_YEAR_TARGET_PRICE-value" in test:
            market_cap_elem = soup.find( 'td', { 'data-test' : 'ONE_YEAR_TARGET_PRICE-value' } )
            market_cap = market_cap_elem.text
            market_cap = market_cap.replace(',','')
            market_cap = market_cap.replace('$','')
            interesting_data[key].update({'premo':market_cap})

    with open("stock_data.json", "r+") as file:
        data = json.load(file)
        data.update(interesting_data)
        file.seek(0)
        json.dump(data, file)

def main():
    all_stocks = get_stock_list()

    percetage = input("Give me the percentage for one year grow accepted: ")
    print('\n')
    grow_threaths(all_stocks, percetage, grow_measurement)

    one_y_premonition_yahoo()

    with open("stock_data.json", 'r') as outfile:
        interesting_data = json.loads(outfile.read())
        pprint(interesting_data)

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
