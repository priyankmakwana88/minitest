#!/usr/bin/env python3


#IMPORT LIBRARIES
import numpy as np
from bs4 import BeautifulSoup
import requests
import speech_recognition as sr
import webbrowser as wb
import os
from gtts import gTTS


#RECEIVING AUDIO
r=sr.Recognizer()

with sr.Microphone() as  source:
	r.adjust_for_ambient_noise(source)
	print ("What is your favroute song?")
	audio=r.listen(source)

try:
	
	speak=r.recognize_google(audio)
	
	#VOICE DATA CLEANING
	final_string=''
	stripped_data=speak.strip()	#____Removing extra spaces
	final_data=stripped_data.split()#____Fetching individual words
	print(final_data)
	
	#CREATING USABLE LINK FROM CLEANED DATA
	for i in final_data:
		final_string=final_string+i+'+'	
	last=len(final_string)
	final_string=final_string[:last-1]
	url_new="http://www.google.com/search?q="+final_string
	print (url_new)
	
	
	#SCRAPPING FOR USEABLE LINK
	page = requests.get(url_new)
	#page = urllib2.urlopen(url_new)

	html_source=page.text
	
	#constructing beautifulsoup constructer
	soup=BeautifulSoup(html_source,'html.parser')
	#soup=BeautifulSoup(page,'html.parser')
	sorted_page=soup.prettify()


	cite_pos=sorted_page.find('<cite')
	http_pos=sorted_page.find('http',cite_pos+1)
	end_cite_pos=sorted_page.find('</cite>',http_pos+1)
	link=sorted_page[http_pos:end_cite_pos]
	
	new_link=link.split()
	#print(new_link)
	'''	
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
	


	#OPENING THE LINK(PLAYING SONG)
	wb.open_new_tab(new_link[0])
		
	
	
except:
	print("Could Not Understand!!")
	pass



