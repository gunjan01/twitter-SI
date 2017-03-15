#!/usr/bin/python
import tweepy
import matplotlib.pyplot as plt
import urllib2
import json

from mechanize import Browser
from BeautifulSoup import BeautifulSoup
def twitterRating(name):
	c_key=''
	c_secret=''
	a_token=''
	a_secret=''

	OAUTH_KEYS={'consumer_key':c_key, 'consumer_secret':c_secret, 'access_token_key':a_token, 'access_token_secret':a_secret}

	auth=tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'],OAUTH_KEYS['consumer_secret'])
	api=tweepy.API(auth)

	
	results=[]
	results=api.search(q=name)

	for tweet in tweepy.Cursor(api.search,q=name).items(1):
		results.append(tweet)

	#process tweet
	
	def process_tweet(tweet):
		#tweet=tweet.lower()
		tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
	    	#Convert @username to AT_USER
	   	tweet = re.sub('@[^\s]+','AT_USER',tweet)
	   	 #Remove additional white spaces
	   	tweet = re.sub('[\s]+', ' ', tweet)
	   	 #Replace #word with word
	    	tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
	    	#trim
	    	tweet = tweet.strip('\'"')
	    	return tweet
	

	#values = {'data': [{'text': 'I love Titanic.'}, {'text': 'I hate Titanic.'}, {'text':'T titanic'}]}
	data=[]

	for each in results:
	  data.append({"text":each.text})

	values = {'data': data}

	headers = {'content-type':'application/json'}
	url = 'http://www.sentiment140.com/api/bulkClassifyJson?appid=punarvasu510@gmail.com'
	response = urllib2.urlopen(url, json.dumps(values))
	output = response.read()
	output = json.loads(output)

	plot=[]
	for each in output["data"]:
		#print each["polarity"]
	  	plot.append(each["polarity"])


	p=0
	n=0
	ne=0
	irr=0
	for item in plot:
		if item==4:
			p=p+1
		elif item==2:
			ne=ne+1
		elif item==0:
			n=n+1
		else:
		     irr=irr+1

	p=(float(p)/len(plot))
	n=(float(n)/len(plot))
	ne=(float(ne)/len(plot))
	irr=(float(irr)/len(plot))
	print p		
	print n
	print ne
	print irr


	tr=p/(p+n+ne+irr)

	return tr
