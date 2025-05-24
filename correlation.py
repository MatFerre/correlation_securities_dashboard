import pandas as pd
import numpy as np
import yfinance as yf

# Define tickers and dates
tickers = ["AAPL", "TSLA", "MSFT", "GOOGL"]
index_ticker = "SPGI"
start_date = pd.to_datetime("2020-01-01")
end_date = pd.to_datetime("2025-01-01")

# Download stock data (only 'Close' prices)
data = yf.download(tickers, start=start_date, end=end_date)["Close"]

# Download index data (only 'Close' prices)
index = yf.download(index_ticker, start=start_date, end=end_date)["Close"]

# Calculate daily returns
returns = data.pct_change().dropna()

returns
