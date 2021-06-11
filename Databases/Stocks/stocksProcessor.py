from Databases.DatabaseGenerator import Database
import yfinance as yf

DATABASE = Database("Stocks", 1)
STOCKS = "./Databases/Stocks/stock-tickers.txt"

with open(STOCKS) as f:
  for line in f:
    ticker = line.split()[0]
    if len(ticker) == 3:
      try:
        t = yf.Ticker(ticker)
        print(ticker, "-", t.info['shortName'])

        DATABASE.add(ticker, (t.info['shortName'], t.info['website'], t.info['longBusinessSummary'], ""))
      except Exception as e:
        print(ticker, e)
      # print(result['link'].split("=", 1)[1])


# msft = yf.Ticker("MSFT")

# # get stock info
# msft.info

# # get historical market data
# hist = msft.history(period="max")

# # show actions (dividends, splits)
# msft.actions

# # show dividends
# msft.dividends

# # show splits
# msft.splits

# # show financials
# msft.financials
# msft.quarterly_financials

# # show major holders
# msft.major_holders

# # show institutional holders
# msft.institutional_holders

# # show balance sheet
# msft.balance_sheet
# msft.quarterly_balance_sheet

# # show cashflow
# msft.cashflow
# msft.quarterly_cashflow

# # show earnings
# msft.earnings
# msft.quarterly_earnings

# # show sustainability
# msft.sustainability

# # show analysts recommendations
# msft.recommendations

# # show next event (earnings, etc)
# msft.calendar

# # show ISIN code - *experimental*
# # ISIN = International Securities Identification Number
# msft.isin

# # show options expirations
# msft.options
