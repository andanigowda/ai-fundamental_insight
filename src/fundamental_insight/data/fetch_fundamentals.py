import yfinance as yf

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    return stock.info