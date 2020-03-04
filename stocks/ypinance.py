from pprint import pprint
import yfinance as yf

msft = yf.Ticker("TSLA")

# get stock info
stock_last_close = msft.info['previousClose']
print(stock_last_close)

# get historical market data
#hist = msft.history(period="5y")
#pprint(hist)

# show major holders
#print(msft.major_holders)

# show institutional holders
#print(msft.institutional_holders)

# show analysts recommendations
#print(msft.recommendations)

