from pprint import pprint
import yfinance as yf

msft = yf.Ticker("TSLA")

# get stock info
#pprint(msft.info)

# get historical market data
#hist = msft.history(period="5y")
#pprint(hist)

# show major holders
#print(msft.major_holders)

# show institutional holders
#print(msft.institutional_holders)

# show analysts recommendations
#print(msft.recommendations)

