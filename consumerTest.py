from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'TW_ANALYSIS',  # Replace with the name of your Kafka topic
    bootstrap_servers=['localhost:9092'],   # Replace with the address of your Kafka broker(s)
    auto_offset_reset='earliest',   # Start reading messages from the beginning of the topic
    enable_auto_commit=True,    # Automatically commit offsets after consuming messages
    group_id='my_group'   # Replace with a unique name for your consumer group
)

# Read messages from the Kafka topic
for message in consumer:
    tweet_dict = json.loads(message.value)
    print(f"Received tweet with id {tweet_dict['id']} from Kafka")
    # Do something with the tweet data, such as storing it in a database or performing some analysis

