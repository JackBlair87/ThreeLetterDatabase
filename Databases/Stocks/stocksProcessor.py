from Databases.DatabaseGenerator import Database
import yfinance as yf

DATABASE = Database("Colleges", 1)
STOCKS = "./Databases/Stocks/stock-tickers.txt"

with open(STOCKS) as f:
  for line in f:
    ticker = line.split()[0]
    if len(ticker) == 3:
      print(ticker)
      msft = yf.Ticker(ticker)
      print(msft.info['shortName'])
      print(msft.info['longBusinessSummary'])


msft = yf.Ticker("MSFT")

# get stock info
msft.info

# get historical market data
hist = msft.history(period="max")

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
msft.financials
msft.quarterly_financials

# show major holders
msft.major_holders

# show institutional holders
msft.institutional_holders

# show balance sheet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options
