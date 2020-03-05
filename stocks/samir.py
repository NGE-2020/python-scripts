import yfinance as yf
import pandas as pd
import lxml
from datetime import datetime, timedelta
import time

last24 = datetime.now - timedelta(days=1)
last24.strftime('%y%m%d')

def comp(stock, deltadate, last=last24):
    today = datetime.now()
    today.strftime('%y%m%d')
    deltadate = deltadate - timedelta(days=1)
    stk = yf.Ticker(stock)
    stk_delta_1 = stk.history(start=today, end=last).iat[0,0]
    stk_delta_2 = stk.history(start=deltadate, end=last).iat[0,0]
    if stk_delta_1 < stk_delta_2:
        increment = stk_delta_2 - stk_delta_1
        pct = (increment / stk_delta_1) * 100
        print('Increment of {:.4f}%'.format(pct))
    else:
        decrement = stk_delta_1 - stk_delta_2
        pct = (decrement / stk_delta_1) * 100
        print('Fall of {:.4f}%'.format(pct))

    return(pct)

comp(msf.history(start='2019-01-02', end='2019-01-03').iat[0,0], msf.history(start='2020-01-02', end='2020-01-03').iat[0,0])
