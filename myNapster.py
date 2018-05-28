#!/usr/bin/env python3


#IMPORT LIBRARIES
import speech_recognition as sr
import os
#from gtts import gTTS
#import pyttsx3


#RECEIVING AUDIO
r=sr.Recognizer()
#engine=pyttsx3.init()
with sr.Microphone() as  source:
	r.adjust_for_ambient_noise(source)
	print ("Heyyy, Whatsup chief!!!")
	#engine.say("Heyy, whats up chief")
	#engine.say("How can i help you?")
	#engine.runAndWait()
	print("Listening...")	
	audio=r.listen(source)

try:
	
	speak=r.recognize_google(audio)
	print(speak)
	#VOICE DATA CLEANING
	stripped_data=speak.strip()	#____Removing extra spaces
	final_data=stripped_data.split()#____Fetching individual words
	print(final_data)
	
	if 'create' in final_data:
		for i in range(0,len(final_data)):
			if final_data[i]=='directory':
				dir_name=final_data[i+1]
				break
	if dir_name:
		os.system('mkdir '+dir_name)
	else:
		print("try again!")
	
except:
	print("Could Not Understand!!")
	pass



