#!/usr/bin/env python3

#IMPORTING LIBRARIES
import tweepy
from textblob import TextBlob
import string
from nltk.corpus import stopwords

words=stopwords.words('english')

#SETTING CUSTOMER AND ACCESS KEY
customer_key=''
customer_secret=''

access_token=''
access_token_secret=''


#AUTHENTICATION
auth=tweepy.OAuthHandler(customer_key,customer_secret)
auth.set_access_token(access_token,access_token_secret)

#MAKING CONNECTION
connect=tweepy.API(auth)

#GETTING LIVE DATA VIA TWITTER (DATA COLLECTION)
get_data=connect.search('modi',count=10)

#print(get_data)


for i in get_data:
	data_line=i.text
	print(data_line)
	#(DATA  CLEANING)

	#REMOVING SPECIAL CHARACTERS
	no_special_char=[ i for i in data_line if i not in string.punctuation]
	no_special_str=''.join(no_special_char)
	#REMOVING STOPWORDS
	li=no_special_str.split()
	no_stop_char=[ i for i in li if i not in words]
	no_stop_str=' '.join(no_stop_char)

	analysis=TextBlob(data_line)
	print(no_stop_str)
	print(analysis.sentiment)
	print('\n')

