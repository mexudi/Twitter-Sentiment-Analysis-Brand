import re
import demoji


# Remove URLs
tweet = re.sub(r'http\S+', '', tweet)
tweet = re.sub(r'bit.ly/\S+', '', tweet)
tweet = tweet.strip('[link]')

# Remove punctuation
my_punctuation = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~•@â'
tweet = re.sub('[' + my_punctuation + ']+', ' ', tweet)

# Remove numbers
tweet = re.sub('([0-9]+)', '', tweet)

# Remove hashtags
tweet = re.sub('(#[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)

# Remove emojis
tweet = demoji.replace(tweet,'')

# Remove extra whitespace
tweet = re.sub('\s+', ' ', tweet).strip()


