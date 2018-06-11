#!/usr/bin/env python3

#IMPORTING LIBRARIES
import urllib.request as ur
from bs4 import BeautifulSoup 
from nltk.tokenize import word_tokenize,sent_tokenize
import numpy as np


website="https://www.news18.com/cricketnext/newstopics/live-cricket-score.html"

web_data=ur.urlopen(website)

source_code=web_data.read()

clean_data=BeautifulSoup(source_code,'html5lib')
#print (clean_data)
#clean_data1=clean_data.prettify()
final_data=clean_data.get_text()
final_data1=BeautifulSoup(final_data,'html5lib')
fd=final_data1.prettify()
#print(type(fd))

#print(fd.split())


#q=[]
#for i in fd:
#	print(i)#.split()
	#if len(j)==0:
	#	continue
	#q.append(j)

#print(q)

#q=word_tokenize(fd)
z=sent_tokenize(fd)
#w=np.asarray(q)
#x=np.asarray(z)
#print(np.shape(w))
'''
for g in range(0,len(z)):
	if len(z[g])==0:
		continue
	else:
		a=z[g].strip()
		print (a)
'''

print(z[3])
#print(np.shape(x))
