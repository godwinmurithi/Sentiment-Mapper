import tweepy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nltk.stem.porter import PorterStemmer
from wordcloud import WordCloud
import json
from collections import Counter
import csv #Import csv

# set auth
consumer_key = "##"
consumer_secret = "##"
access_token = "##"
access_token_secret = "##"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)




#Defining Search keyword and number of tweets and searching tweets
api = tweepy.API(auth, wait_on_rate_limit=True)



csvFile = open('results.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search_tweets,
                           q = "gachagua OR Ruto OR Raila OR Martha OR Asimio OR UDA OR Kenya Kwanza",
                           
                           lang = "en").items():

    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print (tweet.created_at, tweet.text)
csvFile.close()
