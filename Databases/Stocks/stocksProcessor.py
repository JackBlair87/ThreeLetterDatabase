from Databases.DatabaseGenerator import Database
import yfinance as yf

DATABASE = Database("Stocks", 1)
STOCKS = "./Databases/Stocks/stock-tickers.txt"

# print(repr(DATABASE))
print("Stocks Database Complete")

# with open(STOCKS) as f:
#   for line in f:
#     ticker = line.split()[0]
#     if len(ticker) == 3:
#       try:
#         t = yf.Ticker(ticker)
#         print(ticker, "-", t.info['shortName'])

#         DATABASE.add(ticker, (t.info['shortName'], t.info['website'], t.info['longBusinessSummary'], ""))
#       except Exception as e:
#         print(ticker, e)
