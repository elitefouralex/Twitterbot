#MUST USE ATLEAST 3 AND NOT HAVE A SCRIPT WITH THE NAME AS EMAIL.PY IN THE SAME DIRECTORY

import os
import tweepy
import time

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
newtime = time.strftime("%A %B %d, %Y and its %X %Z",time.localtime())
#get input
whattolookfor = input("What keyword would you like to look for?\n>")
numberofTweets = int(input("How many tweets would you like to retweet?\n>")) 


user = api.me()
print(user.name)
print(f"Current time {newtime}")
print(f"Retweeting {numberofTweets} tweets that contain {whattolookfor}.")
 
def main():
    search = (whattolookfor)

    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
main()
