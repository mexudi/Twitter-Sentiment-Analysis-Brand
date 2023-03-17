from kafka import KafkaProducer
import snscrape.modules.twitter as sntwitter
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda m: json.dumps(m).encode('utf-8'))

# Twitter keyword search
keyword = "MXSoufian"
topic_name = 'TW_ANALYSIS'
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f"from:{keyword}").get_items()):
    if i > 1:
        break
    tweet_dict = {
        "id": tweet.id,
        "date": tweet.date.strftime('%Y-%m-%d %H:%M:%S'),
        "content": tweet.rawContent,
        "username": tweet.user.username,
        "replyCount": tweet.replyCount,
        "retweetCount": tweet.retweetCount,
        "likeCount": tweet.likeCount
    }
    # Send the tweet data to Kafka topic
    producer.send(topic_name, value=tweet_dict)
    print(f"Sent tweet with id {tweet.id} to Kafka")

# Wait for any outstanding messages to be delivered and delivery reports received
producer.flush()

