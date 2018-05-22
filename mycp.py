#!/usr/bin/env python3

'''
VERSION 1.0  (MAY 22)

'''

#IMPORT LIBRARIES
import os
from os import mkdir
import sys


#TAKING COMMAND LINE INPUT
user_ip=sys.argv[:]
source_file=user_ip[1]
dest_file=user_ip[2]


#FINDING DESTINATION PATH FROM FILE_NAME
i=0
p=-1
while i<len(dest_file):
	p=dest_file.find('/',i+1)
	if p>0:
		i=p
	else:
		break
dest_loc=dest_file[:i+1]
dest_file_name=dest_file[i+1:]


#FINDING SOURCE FILE NAME FROM FILE_NAME
i=0
p=-1
while i<len(source_file):
	p=source_file.find('/',i+1)
	if p>0:
		i=p
	else:
		break
source_file_name=source_file[i:]


#APPENDING THE SOURCE FILE NAME IF DESTINATION FILE IS NOT AVAILABLE
if not dest_file_name:
	dest_file=dest_loc+source_file_name
	


#CHECKING FOR SOURCE FILE EXISTANCE
if os.path.exists(source_file):
	
	#CHECK DESTINATION VALIDITY
	if os.path.exists(dest_loc):
				
		#CHECKING IF THE FILE IS DIRECTORY
		if os.path.isdir(source_file):		
			
			#COPYING DIRECTORY	
			print("Directory copy successful!!!")
			mkdir(dest_file)
				
		else:
			#COPYING FILE
			print("Copy successful!!!")
			#READING SOURCE FILE
			source_f=open(source_file_name)
			data_source=source_f.read()
			source_f.close()
			
			#CREATING DESTINATION FILE
			dest_f=open(dest_file,'w')
			dest_f.write(data_source)
			dest_f.close()
						

	else:
		print('INVALID DESTINATION')

else:
	print("FILE WITH SUCH NAME DOES NOT EXIST AT THE LOCATION!!!")


