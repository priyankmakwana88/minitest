#!/usr/bin/env python3

#IMPORT LIBRARIES
import numpy as np
import urllib.request as ur
from bs4 import BeautifulSoup

url_ip=input("Enter the url : ")
url_new="http://"+url_ip
page = ur.urlopen(url_new)


#constructing beautifulsoup constructer
soup=BeautifulSoup(page,'html.parser')

for link in soup.find_all('a'):
	links=link.get('href')
	if links.find('http')==0:
		print(links)

