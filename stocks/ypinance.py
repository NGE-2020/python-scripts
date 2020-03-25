from pprint import pprint
import yfinance as yf

msft = yf.Ticker("BABA")

# get stock info
stock_last_close = msft.info['previousClose']
fiftyTwo_Week_High = msft.info
twoHundredDayAverage = msft.info['twoHundredDayAverage']

pprint(fiftyTwo_Week_High)

# get historical market data
# hist = msft.history(period="3mo")
# pprint(hist)

# show major holders
#print(msft.major_holders)

# show institutional holders
#print(msft.institutional_holders)

# show analysts recommendations
#print(msft.recommendations)
