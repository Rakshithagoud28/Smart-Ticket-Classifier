from textblob import TextBlob

def score_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity
