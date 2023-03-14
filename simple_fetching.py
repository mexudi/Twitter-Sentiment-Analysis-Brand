import snscrape.modules.twitter as sntwitter
import pandas as pd
# Define the search term
search_term = "NBA"

# Using TwitterSearchScraper to scrape data and append tweets to list
tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{search_term} since:2021-01-01 until:2021-03-01').get_items()):
    if i>10:
        break
    tweets.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username])

# Print the tweets
tweets_df = pd.DataFrame(tweets, columns=["Datetime", "id","Tweet","User"])
tweets_df.to_csv('term.csv')
