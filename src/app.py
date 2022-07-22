#pip install tweepy
import tweepy 
import requests

userkey='wZHyt0zmjQho8U3Db5ws5z52p'
keysecret='8wlKAA92gcSyVfAgLxChVVRQ5PiV61JwIeZHKLmhzwkabz2fV7'
bearertoken='AAAAAAAAAAAAAAAAAAAAACKGdwEAAAAABXLmtxnxH%2FhGvMK6KJGk5UQxJeE%3D8dddsAMNXHhUMWHzG6gUVZArPnc6BvAB4SzwuyZkZp2EGlU99E'


#client=tweepy.Client(bearer_token=bearertoken, consumer_key=userkey, consumer_secret='202753071-aSAV4jAEZcJ3TPOWEwVhYBj7ZeArdtWCqmEDwAqW', access_token=keysecret, access_secret='7XaXXeJsgukicNuwsBBbu1eP41AnfBliPv68VQIxnH1Dj', return_type= requests.Response, weit_on_reit_limit=True)

client = tweepy.Client(bearer_token=bearertoken,
consumer_key="wZHyt0zmjQho8U3Db5ws5z52p",
consumer_secret="AAAAAAAAAAAAAAAAAAAAACKGdwEAAAAABXLmtxnxH%2FhGvMK6KJGk5UQxJeE%3D8dddsAMNXHhUMWHzG6gUVZArPnc6BvAB4SzwuyZkZp2EGlU99E",
access_token="202753071-aSAV4jAEZcJ3TPOWEwVhYBj7ZeArdtWCqmEDwAqW",
access_token_secret="202753071-aSAV4jAEZcJ3TPOWEwVhYBj7ZeArdtWCqmEDwAqW",
return_type=requests.Response,
wait_on_rate_limit=True
)

query='#100daysofcode (pandas OR python) -is:retweet'

query

tweets=client.search_recent_tweets(query=query,tweet_fields=['author_id','created_at','lang'],max_results=100)

tweets_json=tweets.json()

print(tweets_json)

import pandas as pd

tweets_data=tweets_json['data']
df=pd.json_normalize(tweets_data)
print(df)
