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

    clean_data = []
    for stock in stocks:
        if "^" in stock:
            stock = stock.replace("^", "-")
            stock = stock.replace(".", "-")
            clean_data.append(stock)
        else:
            clean_data.append(stock)

    clean_data = clean_data[:10]
    print("Will work with the following list: \n\n",clean_data,"\n")
    return(clean_data)

def grow_measurement(all_stocks):
    interesting_data = {}
    percetage = input("Give me the percentage for one year grow accepted: ")
    print('\n')
    for stock in all_stocks:
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
            # print("The anual grow for {share} is {anual}%\n".format(share=stock,anual=anual_grow))
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

    return(interesting_data)

def one_y_premonition_yahoo(interesting_data):

    final_data = interesting_data

    for key,value in final_data.items():
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
            final_data[key].update({'premo':market_cap})

    print("\nThe intersting data as follows: \n")
    for key,value in final_data.items():
        print("Values for: " + key + "\n")
        pprint(value)
        print('\n')

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

    interesting_data = grow_measurement(all_stocks)

    final_data = one_y_premonition_yahoo(interesting_data)

    # top20_list = get_stock_data(all_stocks)

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
