#!/usr/bin/env python3

#IMPORT LIBRARIES
import numpy as np
#import urllib.request as ur
from bs4 import BeautifulSoup
import requests

url_ip=input("Enter the url : ")

url_new="http://"+url_ip

page = requests.get(url_new)
#page = ur.urlopen(url_new)

html_source=page.text

#constructing beautifulsoup constructer
soup=BeautifulSoup(html_source,'html.parser')
sorted_page=soup.prettify()

print(sorted_page)


'''
#FINDING LINKS
del_pos=[]

while sorted_page.find('<cite') >0:
	cite_pos=sorted_page.find('<cite')
	http_pos=sorted_page.find('http',cite_pos+1)
	end_cite_pos=sorted_page.find('</cite>',http_pos+1)
	link=sorted_page[http_pos:end_cite_pos]
	
	#TO REMOVE <B> TAGS INCLUDED IN link
	new_link=link.split()
	i=0	
	len_list=len(new_link)
	while i < len_list:
		if new_link[i]=='<b>' or new_link[i]=='</b>':
			del_pos.append(i)
		i=i+1
	del_pos.reverse()
	for j in del_pos:
		del new_link[j]
	del del_pos[:]

	#CREATING STRING FROM LIST
	link_final=''
	for i in new_link:
		link_final=link_final+i		

	print(link_final)
	print('')
	#link_final=''
	sorted_page=sorted_page[end_cite_pos+6:]
'''


'''
for link in soup.find_all('a'):
	links=link.get('href')
	#if links.find('http')==0:
	print(links)
'''
