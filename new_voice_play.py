#!/usr/bin/env python3


#IMPORT LIBRARIES
import numpy as np
#from bs4 import BeautifulSoup
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
	url_new="http://www.youtube.com/results?search_query="+final_string
	print (url_new)
	
	
	#SCRAPPING FOR USEABLE LINK
	page = requests.get(url_new)
	
	html_source=page.text
	#print(html_source)
	
	link_code=html_source.find('watch?v=')
	end_quote=html_source.find('"',link_code)
	watch_link=html_source[link_code:end_quote]
	print(watch_link)
	
	#OPENING THE LINK(PLAYING SONG)
	wb.open_new_tab('http://www.youtube.com/'+watch_link)
		
	
	
except:
	print("Could Not Understand!!")
	pass



