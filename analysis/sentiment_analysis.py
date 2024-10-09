from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# Initialize VADER sentiment analyzer
vader_analyzer = SentimentIntensityAnalyzer()

def vader_sentiment_analysis(text):
    """Analyze sentiment using VADER."""
    scores = vader_analyzer.polarity_scores(text)
    return scores['compound'], scores

def textblob_sentiment_analysis(text):
    """Analyze sentiment using TextBlob."""
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity
