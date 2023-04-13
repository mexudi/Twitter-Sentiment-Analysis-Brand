from flask import Flask, render_template
from kafka import KafkaConsumer
import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from flask_socketio import SocketIO

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

@socketio.on('connect')
def handle_connect():
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

        # Emit positive and negative tweet percentages to client
        total_count = positive_count + negative_count
        positive_percent = round(positive_count / total_count * 100, 2)
        negative_percent = round(negative_count / total_count * 100, 2)
        socketio.emit('update_dashboard', {'positive': positive_percent, 'negative': negative_percent})

        # Break out of loop after analyzing 100 tweets
        if positive_count + negative_count == 100:
            break

@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
