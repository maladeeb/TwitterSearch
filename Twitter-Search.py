import twitter
import json

# Function: Search twitter for any keyword(s)

# You can search any combination of keywords and even identify the 
# impression. Examples: "Virgin AND America AND Airlines OR Flight OR Air" or "Egypt AND Killed AND :("
# Details on the Search Operators you can use here: http://tiny.cc/gafu1w


# Before starting, visit the Twitter developer page and create a new application: https://dev.twitter.com/apps/new
# Twitter will assign your application a consumer Key, consumer secret, oauth token, and oauth token secret. 

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET) 

twitter_api = twitter.Twitter(auth=auth)

pyresponse = dict(twitter_api.search.tweets(q=''))

statuses =  pyresponse["statuses"]

for i in range(10):
  print statuses[i]["text"] + '\n'
