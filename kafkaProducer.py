#Import libraries

import auth_tokens as auth
import tweepy
import loggin


from kafka import kafkaProducer

#Generate kafka producer / localhost and 9092 default ports

producer = kafkaProducer(bootstrap_server=['localhost:9092'])

search_term = 'elon musk'
topic_name = 'TW_ANALYSIS'

def twitter_auth():
    # Create Twitter API authentication object
    authenticate = tweepy.OAuthhandler(consumerKey, consumerSecret)

    # Add access information -access token and access token secret-
    authenticate.set_access_token(accessToken, accessTokenSecret)

    # Create API object
    api = tweepy.API(authenticate, wait_onrate_limit=True)
    return api

