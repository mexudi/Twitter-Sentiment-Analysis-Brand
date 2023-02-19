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


class TweetListener(tweepy.Stream):

    def on_date(self, raw_data):
        logging.info(raw_data)
        producer.send(topic_name, value=raw_data)
        return True

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


    def start_streaming_tweets(self, search_term):
        self.filter(track=search_term, language['en'])

if __name__ == '__main__':
    twitter_stream = TweetListner(consumerKey, consumerSecret, accessToken, accessTokenSecret)
    twitter_stream.start_streaming_tweets(search_term)
