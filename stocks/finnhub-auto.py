import requests
import pprint

# # Get general information of a company. You can query by symbol, ISIN or CUSIP
# r = requests.get('https://finnhub.io/api/v1/stock/profile?symbol=AAPL&bpe83pvrh5rauiikmkl0=')
# pprint.pprint(r.json())
#
# # Get a list of company's executives and members of the Board.
# r = requests.get('https://finnhub.io/api/v1/stock/executive?symbol=AAPL&token=')
# pprint.pprint(r.json())
#
# # Get latest analyst recommendation trends for a company.
# r = requests.get('https://finnhub.io/api/v1/stock/recommendation?symbol=AAPL&token=')
# pprint.pprint(r.json())
#
# # Get latest price target consensus.
# r = requests.get('https://finnhub.io/api/v1/stock/price-target?symbol=NFLX&token=')
# pprint.pprint(r.json())
#
# #Get latest stock upgrade and downgrade.
# r = requests.get('https://finnhub.io/api/v1/stock/upgrade-downgrade?symbol=AAPL&token=')
# pprint.pprint(r.json())
#
# # Get company peers. Return a list of peers in the same country and GICS sub-industry
# r = requests.get('https://finnhub.io/api/v1/stock/peers?symbol=AAPL&token=')
# pprint.pprint(r.json())
#
# # Get company historical quarterly earnings surprise going back to 2000.
# r = requests.get('https://finnhub.io/api/v1/stock/earnings?symbol=AAPL&token=')
# pprint.pprint(r.json())
#
# # Get company key metrics such as growth, price, valuation. Full list of supported fields can be:
# # 10DayAverageTradingVolume	    ==    	10 Day Average Trading Volume
# # 13WeekPriceReturnDaily	    ==    	13 Week Price Return (Daily)
# # 26WeekPriceReturnDaily	    ==    	26 Week Price Return (Daily)
# # 3MonthAverageTradingVolume	    ==    	3 Month Average Trading Volume
# # 52WeekHigh	    ==    	52 Week High
# # 52WeekHighDate	    ==    	52 Week High Date
# # 52WeekLow	    ==    	52 Week Low
# # 52WeekLowDate	    ==    	52 Week Low Date
# # 52WeekPriceReturnDaily	    ==    	52 Week Price Return (Daily)
# # 5DayPriceReturnDaily	    ==    	5 Day Price Return (Daily)
# # assetTurnoverAnnual	    ==    	Asset Turnover (Annual)
# # assetTurnoverTTM	    ==    	Asset Turnover (TTM)
# # beta	    ==    	Beta
# # bookValuePerShareAnnual	    ==    	Book Value (Per Share Annual)
# # bookValuePerShareQuarterly	    ==    	Book Value (Per Share Quarterly)
# # bookValueShareGrowth5Y	    ==    	Book Value Growth Rate (Per Share 5Y)
# # capitalSpendingGrowth5Y	    ==    	Capital Spending growth rate 5 year
# # cashFlowPerShareAnnual	    ==    	Cash Flow (Per Share Annual)
# # cashFlowPerShareTTM	    ==    	Cash Flow (Per Share TTM)
# # cashPerSharePerShareAnnual	    ==    	Cash Per Share (Per Share Annual)
# # cashPerSharePerShareQuarterly	    ==    	Cash Per Share (Per Share Quarterly)
# # currentDividendYieldTTM	    ==    	Current Dividend Yield (TTM)
# # currentEv/freeCashFlowAnnual	    ==    	Current EV/Free Cash Flow (Annual)
# # currentEv/freeCashFlowTTM	    ==    	Current EV/Free Cash Flow (TTM)
# # currentRatioAnnual	    ==    	Current Ratio (Annual)
# # currentRatioQuarterly	    ==    	Current Ratio (Quarterly)
# # dilutedEpsExclExtraTTM	    ==    	Diluted Normalized EPS excl. Extra Items (TTM)
# # dividendGrowthRate5Y	    ==    	Dividend Growth Rate (3Y)
# # dividendPerShare5Y	    ==    	Dividend (Per Share 5Y)
# # dividendPerShareAnnual	    ==    	Dividend (Per Share Annual)
# # dividendsPerShareTTM	    ==    	Dividends (Per Share TTM)
# # dividendYield5Y	    ==    	Dividend Yield (5Y)
# # dividendYieldIndicatedAnnual	    ==    	Dividend Yield
# # ebitdaCagr5Y	    ==    	EBITDA CAGR (5Y)
# # ebitdaInterimCagr5Y	    ==    	EBITDA Interim CAGR (5Y)
# # ebitdAnnual	    ==    	EBITD (Annual)
# # ebitdPerShareTTM	    ==    	EBITD (Per Share TTM)
# # ebitdTTM	    ==    	EBITD (TTM)
# # ebtAnnual	    ==    	Earnings Before Taxes (Annual)
# # ebtNormalizedAnnual	    ==    	Earnings Before Taxes Normalized (Annual)
# # ebtTTM	    ==    	Earnings Before Taxes (TTM)
# # epsBasicExclExtraItemsAnnual	    ==    	EPS Basic excl. Extra Items (Annual)
# # epsBasicExclExtraItemsTTM	    ==    	EPS Basic excl. Extra Items (TTM)
# # epsExclExtraItemsAnnual	    ==    	EPS excl. Extra Items (Annual)
# # epsExclExtraItemsTTM	    ==    	EPS excl. Extra Items (TTM)
# # epsGrowth3Y	    ==    	EPS Growth Rate (3Y)
# # epsGrowth5Y	    ==    	EPS Growth Rate (5Y)
# # epsGrowthQuarterlyYoy	    ==    	EPS Growth (Quarterly YoY)
# # epsGrowthTTMYoy	    ==    	EPS Growth (TTM YoY)
# # epsInclExtraItemsAnnual	    ==    	EPS incl. Extra Items (Annual)
# # epsInclExtraItemsTTM	    ==    	EPS incl. Extra Items (TTM)
# # epsNormalizedAnnual	    ==    	EPS Normalized (Annual)
# # focfCagr5Y	    ==    	Free Operating Cash Flow CAGR (5Y)
# # freeCashFlowAnnual	    ==    	Free Cash Flow (Annual)
# # freeCashFlowPerShareTTM	    ==    	Free Cash Flow (Per Share TTM)
# # freeCashFlowTTM	    ==    	Free Cash Flow (TTM)
# # freeOperatingCashFlow/revenue5Y	    ==    	Free Operating Cash Flow/Revenue (5Y)
# # freeOperatingCashFlow/revenueTTM	    ==    	Free Operating Cash Flow/Revenue (TTM)
# # grossMargin5Y	    ==    	Gross Margin (5Y)
# # grossMarginAnnual	    ==    	Gross Margin (Annual)
# # grossMarginTTM	    ==    	Gross Margin (TTM)
# # inventoryTurnoverAnnual	    ==    	Inventory Turnover (Annual)
# # inventoryTurnoverTTM	    ==    	Inventory Turnover (TTM)
# # longTermDebt/equityAnnual	    ==    	Long Term Debt/Equity (Annual)
# # longTermDebt/equityQuarterly	    ==    	Long Term Debt/Equity (Quarterly)
# # marketCapitalization	    ==    	Market Capitalization
# # monthToDatePriceReturnDaily	    ==    	Month to Date Price Return (Daily)
# # netDebtAnnual	    ==    	Net Debt (Annual)
# # netDebtInterim	    ==    	Net Debt (Interim)
# # netIncomeCommonAnnual	    ==    	Net Income to Common (Annual)
# # netIncomeCommonNormalizedAnnual	    ==    	Net Income Available to Common Normalized (Annual)
# # netIncomeCommonTTM	    ==    	Net Income to Common (TTM)
# # netIncomeEmployeeAnnual	    ==    	Net Income/Employee (Annual)
# # netIncomeEmployeeTTM	    ==    	Net Income/Employee (TTM)
# # netInterestCoverageAnnual	    ==    	Net Interest coverage (Annual)
# # netInterestCoverageTTM	    ==    	Net Interest Coverage (TTM)
# # netMarginGrowth5Y	    ==    	Net Profit Margin Growth Rate (5Y)
# # netProfitMargin%Annual	    ==    	Net Profit Margin % (Annual)
# # netProfitMargin5Y	    ==    	Net Profit Margin (5Y)
# # netProfitMarginTTM	    ==    	Net Profit Margin (TTM)
# # operatingMargin5Y	    ==    	Operating Margin (5Y)
# # operatingMarginAnnual	    ==    	Operating Margin (Annual)
# # operatingMarginTTM	    ==    	Operating Margin (TTM)
# # payoutRatioAnnual	    ==    	Payout Ratio (Annual)
# # payoutRatioTTM	    ==    	Payout Ratio (TTM)
# # pbAnnual	    ==    	Price to Book (Annual)
# # pbQuarterly	    ==    	Price to Book (Quarterly)
# # pcfShareTTM	    ==    	Price to Cash Flow (Per Share TTM)
# # peBasicExclExtraTTM	    ==    	P/E Basic excl. Extra Items (TTM)
# # peExclExtraAnnual	    ==    	P/E excl. Extra Items (Annual)
# # peExclExtraHighTTM	    ==    	P/E excl. Extra Items High (TTM)
# # peExclExtraTTM	    ==    	P/E excl. Extra Items (TTM)
# # peExclLowTTM	    ==    	P/E excl. Extra Items Low (TTM)
# # peInclExtraTTM	    ==    	P/E incl. Extra Items (TTM)
# # peNormalizedAnnual	    ==    	P/E Normalized (Annual)
# # pfcfShareAnnual	    ==    	Price to Free Cash Flow (Per Share Annual)
# # pfcfShareTTM	    ==    	Price to Free Cash Flow (Per Share TTM)
# # pretaxMargin5Y	    ==    	Pretax Margin (5Y)
# # pretaxMarginAnnual	    ==    	Pretax Margin (Annual)
# # pretaxMarginTTM	    ==    	Pretax Margin (TTM)
# # priceRelativeToS&P50013Week	    ==    	Price Relative to S&P500 (13 Week)
# # priceRelativeToS&P50026Week	    ==    	Price Relative to S&P500 (26 Week)
# # priceRelativeToS&P5004Week	    ==    	Price Relative to S&P500 (4 Week)
# # priceRelativeToS&P50052Week	    ==    	Price Relative to S&P500 (52 Week)
# # priceRelativeToS&P500Ytd	    ==    	Price Relative to S&P500 (YTD)
# # psAnnual	    ==    	Price to sales (Annual)
# # psTTM	    ==    	Price to sales (TTM)
# # ptbvAnnual	    ==    	Price to Tangible Book (Annual)
# # ptbvQuarterly	    ==    	Price to Tangible Book (Quarterly)
# # quickRatioAnnual	    ==    	Quick Ratio (Annual)
# # quickRatioQuarterly	    ==    	Quick Ratio (Quarterly)
# # receivablesTurnoverAnnual	    ==    	Receivables Turnover (Annual)
# # receivablesTurnoverTTM	    ==    	Receivables Turnover (TTM)
# # revenueAnnual	    ==    	Revenue (Annual)
# # revenueEmployeeAnnual	    ==    	Revenue/Employee (Annual)
# # revenueEmployeeTTM	    ==    	Revenue/Employee (TTM)
# # revenueGrowth3Y	    ==    	Revenue Growth Rate (3Y)
# # revenueGrowth5Y	    ==    	Revenue Growth Rate (5Y)
# # revenueGrowthQuarterlyYoy	    ==    	Revenue Growth (Quarterly YoY)
# # revenueGrowthTTMYoy	    ==    	Revenue Growth (TTM YoY)
# # revenuePerShareAnnual	    ==    	Revenue per Share (Annual)
# # revenuePerShareTTM	    ==    	Revenue per Share (TTM)
# # revenueShareGrowth5Y	    ==    	Revenue Growth (Per Share 5Y)
# # revenueTTM	    ==    	Revenue (TTM)
# # roaa5Y	    ==    	Return on Average Assets (5Y)
# # roae5Y	    ==    	Return on Average Equity (5Y)
# # roaeTTM	    ==    	Return on Average equity (TTM)
# # roaRfy	    ==    	Return on Assets (Annual)
# # roeRfy	    ==    	Return on Average Equity (Annual)
# # roeTTM	    ==    	Return on Equity (TTM)
# # roi5Y	    ==    	Return on Investment (5Y)
# # roiAnnual	    ==    	Return on Investment (Annual)
# # roiTTM	    ==    	Return on Investment (TTM)
# # tangibleBookValuePerShareAnnual	    ==    	Tangible Book Value (Per Share Annual)
# # tangibleBookValuePerShareQuarterly	    ==    	Tangible Book Value (Per Share Quarterly)
# # tbvCagr5Y	    ==    	Tangible Book Value Total Equity CAGR (5Y)
# # totalDebt/totalEquityAnnual	    ==    	Total Debt/Total Equity (Annual)
# # totalDebt/totalEquityQuarterly	    ==    	Total Debt/Total Equity (Quarterly)
# # totalDebtCagr5Y	    ==    	Total Debt CAGR (5Y)
# # yearToDatePriceReturnDaily	    ==    	Year To Date Price Return (Daily)
#
# r = requests.get('https://finnhub.io/api/v1/stock/metric?symbol=AAPL&metric=margin&token=')
# pprint.pprint(r.json())
#
# # Get a full list of shareholders/investors of a company in descending order of the number of shares held.
# r = requests.get('https://finnhub.io/api/v1/stock/investor-ownership?symbol=AAPL&limit=20&token=')
# pprint.pprint(r.json())
#
# # Get a full list fund and institutional investors of a company in descending order of the number of shares held.
# r = requests.get('https://finnhub.io/api/v1/stock/fund-ownership?symbol=TSLA&limit=20&token=')
# pprint.pprint(r.json())
#
# # Get quote data. Constant polling is not recommended. Use websocket if you need real-time update.
# # o = Open price of the day
# # h = High price of the day
# # l = Low price of the day
# # c = Current price
# # pc = Previous close price
# # t = Timestamp of current daily bar
# r = requests.get('https://finnhub.io/api/v1/quote?symbol=AAPL&token=')
# pprint.pprint(r.json())

# # Get candlestick data for stocks. Coverage:
# r = requests.get('https://finnhub.io/api/v1/stock/candle?symbol=AAPL&resolution=1&from=1572651390&to=1572910590&token=')
# pprint.pprint(r.json())
#
# # Get support and resistance levels for a symbol.
# # Support represents a low level a stock price reaches over time, while resistance represents a high level a stock price reaches over time. Support materializes when a stock price drops to a level that prompts traders to buy. This reactionary buying causes a stock price to stop dropping and start rising. Conversely, resistance materializes when a stock price rises to a level that prompts traders to sell. This selling causes a stock price to stop rising and start dropping.
# r = requests.get('https://finnhub.io/api/v1/scan/support-resistance?symbol=IBM&resolution=D&token=')
# pprint.pprint(r.json())
#
# #Get aggregate signal of multiple technical indicators such as MACD, RSI, Moving Average v.v.
# r = requests.get('https://finnhub.io/api/v1/scan/technical-indicator?symbol=AAPL&resolution=D&token=')
# pprint.pprint(r.json())
#
# # List latest company news by symbol. This endpoint is only available for US companies.
# r = requests.get('https://finnhub.io/api/v1/news/AAPL?token=')
# pprint.pprint(r.json())

#List latest major developments of a company going back 20 years with 12M+ data points. This data can be used to highlight the most significant events. Limit to 200 results/call for Ultimate users, and 20 results/call other plans.
r = requests.get('https://finnhub.io/api/v1/major-development?symbol=AAPL&token=')
pprint.pprint(r.json())

# #Get company's news sentiment and statistics. This endpoint is only available for US companies.
# r = requests.get('https://finnhub.io/api/v1/news-sentiment?symbol=AAPL&token=')
# pprint.pprint(r.json())
