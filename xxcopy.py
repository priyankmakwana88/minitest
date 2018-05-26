#!/usr/bin/env python3

#IMPORT LIBRARIES
import os
from os import mkdir
import sys



#TAKING COMMAND LINE INPUT
user_ip=sys.argv[:]
source=user_ip[1]
dest=user_ip[2]



#COPY FILE FUNCTION
def copy_file(source,dest):

	#READING SOURCE FILE
	source_f=open(source)
	data_source=source_f.read()
	source_f.close()
	
	#CREATING DESTINATION FILE		##(copy file) - (dest path and name) - (souce name) - (append source name to dest) - (dir copy)
	dest_f=open(dest,'w')
	dest_f.write(data_source)
	dest_f.close()


#FINDING DESTINATION PATH FROM FILE_NAME

def find_dpath(dest):
	i=0	
	p=-1
	while i<len(dest):
		p=dest.find('/',i+1)
		if p>0:
			i=p
		else:
			break
	dest_path=dest[:i+1]
	dest_name=dest[i+1:]
	return dest_name,dest_path

#print(dest_path)
#print(dest_name)


#FINDING SOURCE FILE NAME FROM FILE_NAME
def find_spath(source):
	i=0
	p=-1
	while i<len(source):
		p=source.find('/',i+1)
		if p>0:
			i=p
		else:
			break
	source_name=source[i:]
	if source_name.find('/')==0:
		source_name=source_name[1:]
	return source_name
#print(source_name)


#APPENDING THE SOURCE FILE NAME IF DESTINATION FILE IS NOT AVAILABLE
def append(source,dest):
	source_name=find_spath(source)
	dest_name,dest_path=find_dpath(dest)
	if not dest_name:
		if os.path.isdir(source):
			dest=dest_path+source_name
	#print(dest)

#SORTING THE LISTED CONTENT OF DIRECTORY
def sort(content):
	#{CON_LIST} IS THE INTEGETR REP. OF Dir CONTENT
	con_list=[]
	for i in content:
		file = os.getcwd()+'/'+i
		if os.path.isdir(file):
			con_list.append(1)
		else:
			con_list.append(0)

	#print (sq)
	l=len(con_list)
	for i in range(0,l-1):
		for j in range(0,l-i-1):
			if con_list[j]>con_list[j+1]:
				con_list[j],con_list[j+1]=con_list[j+1],con_list[j]
				content[j],content[j+1]=content[j+1],content[j]
	return content,con_list
	

#DIRECTORY COPY FUNCTION
def copy_dir(source,dest):
	mkdir(dest)
	append(source,dest)
	content=os.listdir(source)
	content,con_list=sort(content)
	
	len_content=len(content)
	for i in range(0,len_content):
		if con_list[i]==0:	
			copy_file(source,dest)
		else:
			copy_dir(source,dest)
			return


if os.path.isdir(source) :
	copy_dir(source,dest)
else:
	copy_file(source,dest)
