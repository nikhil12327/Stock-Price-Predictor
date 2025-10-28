# data_fetch.py
# This script is a placeholder that shows how to fetch historical data using yfinance.
# In this repo we include a synthetic sample CSV (data/aapl_sample.csv) for offline use.
try:
    import yfinance as yf
    import pandas as pd
except Exception:
    pass

def fetch_stock_data(ticker='AAPL', start='2015-01-01', end='2025-01-01'):
    '''Fetch historical stock data using yfinance (optional).'''
    df = yf.download(ticker, start=start, end=end)
    df.reset_index(inplace=True)
    return df

if __name__ == '__main__':
    print("This project includes a sample CSV at data/aapl_sample.csv. Use data_fetch.py if you want to fetch live data (yfinance required).")
