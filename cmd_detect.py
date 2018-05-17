#!/usr/bin/env python3

import os

def find(name, path):
	for root, dirs, files in os.walk(path):
		if name in files:
			return 1
		else:
			return 0

#os.path.join(root, name)

user_input=input("Enter : ")

#dest_find=["/bin","/usr/bin/"]


if find(user_input,"/bin/") or find(user_input,"/usr/bin/") :
	#print("COMMAND DETECTED!!")
	os.system(user_input)
	os.system(user_input+" | festival --tts")
else:
	#print("NOT A COMMAND")	
	os.system("echo " +user_input)
