
import pandas as pd 
import re
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


#create function to clean the text
def cleantwts(twt):
    twt = re.sub('https?:\/\/\S+','',twt)
    twt = re.sub('rt','',twt)
    twt = re.sub('#[A-Za-z0-9]+','',twt)
    twt = re.sub('@[A-Za-z0-9]+','',twt)
    twt = re.sub('RT','',twt)
    twt = re.sub('//n','',twt)
    return twt


# #read the data
df = pd.read_csv("Kenya_tweets_00000.csv")

#apply function to clean text
df["cleaned_twts"] = df["text"].apply(cleantwts)


#save the data
pd.to_csv("Kenya_tweets_000001.csv")

# #read the data
# data <- read.csv("raw_data130.csv")

# #select the location column and remove null rows
# new_DF<-subset(data, data$author_location!="")
# geocode

