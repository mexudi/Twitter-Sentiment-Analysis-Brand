from flask import Flask, render_template
from kafka import KafkaConsumer
import json
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize Flask app
app = Flask(__name__)

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

@app.route('/')
def index():
    # Initialize counters for positive and negative tweets
    positive_count = 0
    negative_count = 0

    # Initialize Kafka consumer
    consumer = KafkaConsumer('twitter-topic', bootstrap_servers=['localhost:9092'])

    # Iterate through Kafka topic messages
    for message in consumer:
        # Decode message value from bytes to string
        tweet_json = message.value.decode('utf-8')

        # Load tweet JSON string as dictionary
        tweet_dict = json.loads(tweet_json)

        # Get tweet text
        tweet_text = tweet_dict['content']['text']

        # Analyze tweet sentiment
        sentiment = sia.polarity_scores(tweet_text)

        # Increment positive or negative tweet count based on compound sentiment score
        if sentiment['compound'] >= 0.05:
            positive_count += 1
        elif sentiment['compound'] <= -0.05:
            negative_count += 1

        # Break out of loop after analyzing 100 tweets
        if positive_count + negative_count == 100:
            break

    # Calculate percentages of positive and negative tweets
    total_count = positive_count + negative_count
    positive_percent = round(positive_count / total_count * 100, 2)
    negative_percent = round(negative_count / total_count * 100, 2)

    # Render dashboard template with positive and negative tweet percentages
    return render_template('dashboard.html', positive=positive_percent, negative=negative_percent)

if __name__ == '__main__':
    app.run(debug=True)