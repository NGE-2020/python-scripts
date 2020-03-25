from pprint import pprint
import yfinance as yf

def grow_measurement():
    stocks = []
    with open('stock_data.txt') as stock_string:
        stocks = stock_string.read()
        stocks = stocks.split(',')

    stocks = stocks[13500:14000]
    print("Will work with ", len(stocks), "stocks\n")

    clean_data = ""
    counter = 0
    for stock in stocks:
        counter = counter + 1
        print("\n====== Working with stock {stock} (stock number {num})======".format(stock=stock, num=counter))
        try:
            info = yf.Ticker(stock)
            stock_last_close = info.info['currency']
            clean_data = clean_data + "," + stock

        except IndexError:
            pass
        except ValueError:
            pass
        except ImportError:
            pass
        except NameError:
            pass
        except KeyError:
            pass
        else:
            pass

    print(clean_data)

def main():
    grow_measurement()

if __name__ == '__main__':
    main()
