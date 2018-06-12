#!/usr/bin/env python3

#IMPORTING LIBRARIES
import urllib.request as ur
from bs4 import BeautifulSoup 
from nltk.tokenize import word_tokenize,sent_tokenize
import string as st
import numpy as np
from nltk.corpus import stopwords
from nltk.probability import FreqDist

stop_words=stopwords.words('english')

#------- DATA COLLECTION -------

#WEBSITE FROM WHERE DATA NEED TO BE EXTRACTED
website="https://php.net"

#EXTRACTING SOURCE CODE
web_data=ur.urlopen(website)
source_code=web_data.read()

#SOURCE CODE CLEANING
clean_data=BeautifulSoup(source_code,'html5lib')
final_data=clean_data.get_text(strip=True)


#------- DATA TOKENIZE -------

#TOKENIZE ACC TO WORD
word_split=word_tokenize(final_data)

#TOKENIZE ACC. TO SENTENCE
#sent_split=sent_tokenize(final_data)

#------- DATA CLEANING -------

#REMOVE SPECIAL CHARACTERS
special_free=[i for i in word_split if i not in st.punctuation]

#REMOVE STOPWORDS (COMPARING LOWER CASE)
stop_free=[i for i in special_free if i.lower() not in stop_words]


print(np.shape(special_free))
print(np.shape(stop_free))

#------- DATA PLOTTING -------

freq=FreqDist(stop_free)

freq.plot(10)




