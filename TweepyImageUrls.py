import tweepy
import datetime, time
import twitter_credentials

auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.COMSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def get_tweets(api, username, days : int):
    page = 1
    deadend = False
    while True:
        tweets = tweepy.API(auth).user_timeline(username, page = page, tweet_mode = "extended", count = 200)

        for tweet in tweets:
            if ( datetime.datetime.now() - tweet.created_at).days <= days:
                if tweet.full_text.startswith("RT @") == False and 'media' in tweet.entities and len(tweet.entities['urls']) > 0:
                    for link in tweet.extended_entities['media']:
                        if 'video' not in link['media_url']:
                            print(link['media_url'])
                
            else:
                deadend = True
                return
            
        if not deadend:
            page + 1
            

get_tweets(api, "playboyplus", 15)