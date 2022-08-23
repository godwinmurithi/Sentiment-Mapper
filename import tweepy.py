import tweepy

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
consumer_key = "Rf2lHuEL74VytBbtJUAyeVNd1"
consumer_secret = "PXxmvaVZIvH7bzeDLgbWwif4NyLXWk4gpMAimUG3kpOxr2wdQz"

# Your account's (the app owner's account's) access token and secret for your
# app can be found under the Authentication Tokens section of the
# Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
access_token = "964974181493428224-AdvTVpr6VJP1b4CUqzTiKe6X3VHTe0y"
access_token_secret = "A"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

# If the authentication was successful, this should print the
# screen name / username of the account
print(api.verify_credentials().screen_name)


def get_twitter_location(search):
    api = get_twitter_api()
    count = 0
    for tweet in tweepy.Cursor(api.search_tweets, q="gachagua OR Ruto OR Raila OR Martha OR Asimio OR UDA OR Kenya Kwanza").items(500):
        if hasattr(tweet, 'coordinates') and tweet.coordinates is not None:
            count += 1
            print("Coordinates", tweet.coordinates)
        if hasattr(tweet, 'location') and tweet.location is not None:
            count += 1
            print("Coordinates", tweet.location)
    print(count)
get_twitter_location("gachagua OR Ruto OR Raila OR Martha OR Asimio OR UDA OR Kenya Kwanza")
