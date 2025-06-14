from transformers import pipeline

def analyze_sentiment(news_list):
    model_name = "yiyanghkust/finbert-sentiment"
    sentiment_pipeline = pipeline("sentiment-analysis", model=model_name, tokenizer=model_name)
    return [sentiment_pipeline(text)[0] for text in news_list]
