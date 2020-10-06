import tweepy
import time


print('this is my twitter searchbot')


CONSUMER_KEY = 'j0O27W3VkX5iO4SvKxxcS8Rpj'
CONSUMER_SECRET = 'rgeGmawK1T7ysOcV0hgJNdaPLUW7XUpn7FzhvW3EoxAemNn4vD'
ACCESS_KEY = '1259867690119954432-D5v7Sn1WBrrVkj3ULd9YGaDv7yWuWi'
ACCESS_SECRET = 'emgQhuH7M42YUewgx6thLtAT1J294sHG3PHepCNo6JF0S'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)


hastag = "#icantbreathe"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hastag).items(tweetNumber)

def searchBot():
    for tweet in tweets:
            try:
                tweet.retweet()
                print("Retweet done!")
                time.sleep(5)
            except tweepy.TweepError as e:
                print(e.reason)
                time.sleep(5)

searchBot()