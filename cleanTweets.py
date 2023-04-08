import re
import demoji
import pandas as pd

def cleanTweet(df: pd.DataFrame, column: str) -> pd.DataFrame:
    # Remove URLs
    df[column] = df[column].str.replace(r'http\S+', '', regex=True)
    df[column] = df[column].str.replace(r'bit.ly/\S+', '', regex=True)
    df[column] = df[column].str.strip('[link]')

#     # Remove user mentions
#     df[column] = df[column].str.replace('(RT\s@[A-Za-z]+[A-Za-z0-9-_]+)', '', regex=True)
#     df[column] = df[column].str.replace('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', regex=True)

    # Remove punctuation
    my_punctuation = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~•@â'
    df[column] = df[column].str.replace('[' + my_punctuation + ']+', ' ', regex=True)

    # Remove numbers
    df[column] = df[column].str.replace('([0-9]+)', '', regex=True)

    # Remove hashtags
    df[column] = df[column].str.replace('(#[A-Za-z]+[A-Za-z0-9-_]+)', '', regex=True)

    # Remove emojis
    df[column] = df[column].apply(lambda x: demoji.replace(x,''))

    # Remove extra whitespace
    df[column] = df[column].str.replace('\s+', ' ', regex=True).str.strip()

    return df
