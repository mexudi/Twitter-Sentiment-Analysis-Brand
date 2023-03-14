from kafka import KafkaProducer

# Set up the Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
import snscrape.modules.twitter as sntwitter

# Set up the search criteria
search_terms = 'python'

# Fetch the tweets and send them to Kafka
for tweet in sntwitter.TwitterSearchScraper(search_terms).get_items():
    producer.send('twitter', tweet.content.encode('utf-8'))


# Close the producer
producer.close()

