from pprint import pprint

import time
import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

def takipEttikleri(kadi):
    friendsList=[]
    users = tweepy.Cursor(api.friends, kadi).items()
    while True:
        try:
            user = next(users)
        except tweepy.TweepError:
            print(tweepy.TweepError)
            time.sleep(60 * 15)
            user = next(users)
        except StopIteration:
            break
        friendsList.append(user.screen_name)
        # print("@" + user.screen_name)
    return friendsList


followers = []

def printFollowers(kadi):
    users = tweepy.Cursor(api.followers, kadi).items()
    while True:
        try:
            user = next(users)
        except tweepy.TweepError:
            print(tweepy.TweepError)
            time.sleep(60 * 15)
            user = next(users)
        except StopIteration:
            break
        followers.append(user.screen_name)
        print("@" + user.screen_name)
    return followers


def tweetAl(username):
    tweets = api.user_timeline(username, count=200, include_rts=True, tweet_mode="extended")

    # Empty Array
    tmp = []

    # create array of tweet information: username,
    # tweet id, date/time, text
    tweets_for_csv = [tweet.full_text for tweet in tweets]  # CSV file created
    for j in tweets_for_csv:
        # Appending tweets to the empty array tmp
        tmp.append(j)

        # Printing the tweets
    pprint(tmp)
    # print(tmp.lenght)


def takipEdilenlerdenTweetleriAl(liste):
    for i in liste:
        tweetAl(i)


def retweetle(kadi):
    for tweet in tweepy.Cursor(api.user_timeline, kadi).items():
        try:
            print('\nRetweet Bot tarafından bulunan tweet @' + tweet.user.screen_name + '. ' + 'Retweet ediliyor.')

            tweet.retweet()
            print('Retweet yollandı.')

            # Where sleep(10), sleep is measured in seconds.
            # Change 10 to amount of seconds you want to have in-between retweets.
            # Read Twitter's rules on automation. Don't spam!
            time.sleep(5)

        # Some basic error handling. Will print out why retweet failed, into your terminal.
        except tweepy.TweepError as error:
            print('\nError. Retweet yapılamadı. Sebep: ')
            print(error.reason)

        except StopIteration:
            break

def seriRT(liste):
    for i in liste:
        retweetle(i)

user = 'twitterusername'

print("takipçiler")
# print(printFollowers(user))
fliste = takipEttikleri(user)
print("-------------")
print("tweetler")
tweetAl(user)
print("-------------")
print("takipçi tweetleri")
takipEdilenlerdenTweetleriAl(fliste)
print("-------------")
seriRT(fliste)
print("-------------")

