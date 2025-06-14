from data.fetch_fundamentals import get_stock_info
from data.fetch_news import get_latest_news
from analysis.sentiment import analyze_sentiment
from output.report_generator import save_report

def main():
    ticker = "AAPL"
    info = get_stock_info(ticker)
    news = get_latest_news(ticker)
    sentiments = analyze_sentiment(news)
    save_report(ticker, info, news, sentiments)

if __name__ == "__main__":
    main()
