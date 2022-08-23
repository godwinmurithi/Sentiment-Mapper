import tweeter_api
import configparser
import tweepy
import matplotlib 
import json
import pandas



api_key = "Rf2lHuEL74VytBbtJUAyeVNd1"
api_key_secret = "PXxmvaVZIvH7bzeDLgbWwif4NyLXWk4gpMAimUG3kpOxr2wdQz"
access_token = "964974181493428224-e93mZvsj58u4V6vOLwfD8qr4vhSX7os"
access_token_secret = "aQnoPNbFTU9RAILtKMXjUc0rhfnvSD1TmfFGxhkcahYDB"

auth = tweepy.OAuth1UserHandler(
    api_key, api_key_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

# authenticate
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

import tweepy

stream = tweepy.Stream(
    "Consumer Key here", "Consumer Secret here",
    "Access Token here", "Access Token Secret here"
)


response = api.search_tweets(q=("Ruto", "Raila"), geocode= 37.781157 -122.398720)



coordinates = []
tweets = response.get_iterator()

count = 0

while count < 50:
    tweet = next(tweets)
    if "place" in tweet and tweet["place"] != None:
        place = tweet["place"]["bounding box"]["coordinates"][0][0]
        coordinates.append(place)
        count += 1
        print(place)

import pandas as pd

# create dataframe
columns = ['Time', 'User', 'Tweet','place']

data = []
for tweet in tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text, tweet.place])

df = pd.DataFrame(data, columns=columns)

df.to_csv('tweets.csv')
