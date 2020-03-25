import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint
import yfinance as yf

def grow_measurement():
    stocks = []
    with open('stock_data.txt') as stock_string:
        stocks = stock_string.read()
        stocks = stocks.split(',')

    stocks = stocks[0:20]
    print("Will work with ", len(stocks), "stocks\n")

    interesting_data = {}
    percetage_grow = input("Give me the percentage for one year grow accepted: ")
    percetage_loss = input("Give me the percentage for two months loss accepted: ")
    print('\n')
    counter = 0
    for stock in stocks:
        counter = counter + 1
        print("\n====== Working with stock {stock} (stock number {num})======".format(stock=stock, num=counter))
        try:
            info = yf.Ticker(stock)
            oney_hist = info.history(period="1y")
            oney_hist_string = str(oney_hist)
            oney_hist_list1 = oney_hist_string.split('\n')
            oney_hist_list2 = oney_hist_list1[2].split(' ')
            last_year =  float(oney_hist_list2[4])

            bim_hist = info.history(period="2mo")
            bim_hist_string = str(bim_hist)
            bim_hist_list1 = bim_hist_string.split('\n')
            bim_hist_list2 = bim_hist_list1[2].split(' ')
            bim =  float(bim_hist_list2[4])

            stock_last_close = info.info['previousClose']
            week52_High = info.info['fiftyTwoWeekHigh']
            ask = info.info['ask']
            bid = info.info['bid']

            anual_grow = ((stock_last_close*100)/last_year) - 100
            anual_grow = round(anual_grow, 2)

            bim_loss = 100 - ((stock_last_close*100)/bim)
            bim_loss = round(bim_loss, 2)

            if anual_grow >= float(percetage_grow):
                interesting_data.update({stock:{'anual_grow':anual_grow}})
                interesting_data[stock].update({'bim_loss':bim_loss})
                interesting_data[stock].update({'actual':stock_last_close})
                interesting_data[stock].update({'week52_High':week52_High})
                interesting_data[stock].update({'ask':ask})
                interesting_data[stock].update({'bid':bid})

            if bim_loss >= float(percetage_loss):
                interesting_data.update({stock:{'anual_grow':anual_grow}})
                interesting_data[stock].update({'bim_loss':bim_loss})
                interesting_data[stock].update({'actual':stock_last_close})
                interesting_data[stock].update({'week52_High':week52_High})

        except IndexError:
            # clean_data.remove(stock)
            pass
        except ValueError:
            # clean_data.remove(stock)
            pass
        except ImportError:
            # clean_data.remove(stock)
            pass
        except NameError:
            # clean_data.remove(stock)
            pass
        else:
            pass

    pprint(interesting_data)

    # with open("stock_data.json", 'w') as outfile:
    #     outfile.write(json.dumps(interesting_data))
    #
    # final_list = ""
    # for stock in clean_data:
    #     final_list = final_list + "," + stock
    #
    # print(len(final_list))
    # print(final_list)

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

    # with open("stock_data_final.json", 'w') as outfile:
    #     outfile.write(json.dumps(interesting_data))

    with open("stock_data_final.json", "r+") as file:
        data = json.load(file)
        data.update(interesting_data)
        file.seek(0)
        json.dump(data, file)

def main():
    grow_measurement()
    # one_y_premonition_yahoo()
    # with open("stock_data_final.json", 'r') as outfile:
    #     interesting_data = json.loads(outfile.read())
    #     pprint(interesting_data)

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
