from textblob import TextBlob
import pandas as pd

# TextBlob Subjectivity function
def Subjectivity(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df['subjectivity'] = df[column].apply(lambda x: TextBlob(x).sentiment.subjectivity)
    return df

# TextBlob Polarity function
def Polarity(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df['polarity'] = df[column].apply(lambda x: TextBlob(x).sentiment.polarity)
    return df

# Assign sentiment to elements
def Sentiment(df: pd.DataFrame, polarity_column: str, sentiment_column: str) -> pd.DataFrame:
    df[sentiment_column] = df[polarity_column].apply(lambda x: 'Negative' if x < 0 else ('Neutral' if x == 0 else 'Positive'))
    return df

