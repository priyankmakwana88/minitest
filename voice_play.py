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
	print ("What is your favroute song?")
	audio=r.listen(source)

try:
	
	speak=r.recognize_google(audio)
	
	#VOICE DATA CLEANING
	final_string=''
	stripped_data=speak.strip()	#____Removing extra spaces
	final_data=stripped_data.split()#____Fetching individual words

	#CREATING USABLE LINK FROM CLEANED DATA
	for i in final_data:
		final_string=final_string+i+'+'	
	last=len(final_string)
	final_string=final_string[:last-1]
	url_new="http://www.google.com/search?q="+final_string
	print (url_new)

	#SCRAPPING FOR USEABLE LINK

	#FETCHING SOURCE CODE
	page = requests.get(url_new)
	html_source=page.text
	soup=BeautifulSoup(html_source,'html.parser')
	sorted_page=soup.prettify()
	#EXTRACTING REQUIRED LINK
	cite_pos=sorted_page.find('<cite')
	http_pos=sorted_page.find('http',cite_pos+1)
	end_cite_pos=sorted_page.find('</cite>',http_pos+1)
	link=sorted_page[http_pos:end_cite_pos]
	new_link=link.split()
	
	#CREATING MACHINE RESPONSE	
	tts = gTTS(text="Playing "+speak, lang='en')
	tts.save("good.mp3")
	os.system("mpg321 good.mp3 ")	
		
	#OPENING THE LINK(PLAYING SONG)
	wb.open_new_tab(new_link[0])
	
	
	
except:
	print("Could Not Understand!!")
	pass



