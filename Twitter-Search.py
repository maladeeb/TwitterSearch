import twitter
import json

# Function: Search twitter for any keyword(s)

# You can search any combination of keywords and even identify the 
# impression. Examples: "Virgin AND America AND Airlines OR Flight OR Air" or "Egypt AND Killed AND :("
# Details on the Search Operators you can use here: http://tiny.cc/gafu1w


# Before starting, visit the Twitter developer page and create a new application: https://dev.twitter.com/apps/new
# Twitter will assign your application a consumer Key, consumer secret, oauth token, and oauth token secret. 

CONSUMER_KEY = 'NgbX33wZQedC6dZQFroduQ'
CONSUMER_SECRET = 'Z44OVbKPXmtiSxxTXV3x5ol50a6H47KWym8MFOY'
OAUTH_TOKEN = '18477675-MajhhOjq2h6fmrQt45DaRVWdwlqT0TEi4V5qtrK2k'
OAUTH_TOKEN_SECRET = 'GDSAfLLLDwN29Q7dIn7Y5zHvARuJ1MkZ47z2CLYlmw'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET) 

twitter_api = twitter.Twitter(auth=auth)

pyresponse = dict(twitter_api.search.tweets(q='Egypt AND Brotherhood AND :('))

statuses =  pyresponse["statuses"]

for i in range(10):
  print statuses[i]["text"] + '\n'
