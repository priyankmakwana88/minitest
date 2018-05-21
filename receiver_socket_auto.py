#!/usr/bin/env python

import socket
import numpy as np
import time
import netifaces as ni
import matplotlib.pyplot as plt


recv_ip=ni.ifaddresses("wlp9s0")[ni.AF_INET][0]['addr']
#recv_ip =ni.ifaddresses("eth0")[ni.AF_INET][0]['addr']



#timeout2 = time.time() + 30

#recv_ip='127.0.0.1'
port=8888

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((recv_ip,port))

total_hi_list=[]
total_hello_list=[]

hi=[]
hello=[]

#while time.time() < timeout2:

for i in (0,1):
	timeout = time.time() + 15
	while time.time() < timeout:
		#EXTRACT MESSAGE AND CREATE A LIST
		data_rec=s.recvfrom(1000)
		msg_received=data_rec[0]
		strip_msg=msg_received.strip()
		split_msg=strip_msg.split()

		#print(strip_msg)
		#print(split_msg)	

		
		#COUNT NO. OF HI & HELLO
		total_hi=0
		total_hello=0
		hi_count=0
		hello_count =0
		for i in range(0,len(split_msg)):
			if split_msg[i]=='hi':
				hi_count=hi_count+1
			elif split_msg[i]=='hello':
				hello_count=hello_count+1
	
	
		#MAINTAINING HI AND HELLO VARIABLES
		hi.append(hi_count)
		hello.append(hello_count)
#print(hi)
#print(hello)
	
	for i in range(0,len(hi)):
		total_hi=total_hi+hi[i]
	for i in range(0,len(hello)):
		total_hello=total_hello+hello[i]
	del hi[:]
	del hello[:]

	total_hi_list.append(total_hi)
	total_hello_list.append(total_hello)
	
print(total_hi_list)
print(total_hello_list)
print(total_hi_list[1])
print(total_hello_list[1])
	
#DRAWING GRAPH
plt.figure(1)
plt.subplot(131)
plt.suptitle("no('HI') vs no('HELLO') - PHASE 1")
plt.xlabel("no('HI')")	
plt.ylabel("no('HELLO')")
plt.bar(total_hi_list[0],total_hello_list[0])
plt.show()

plt.subplot(132)
plt.title("no('HI') vs no('HELLO') - PHASE 2")
plt.xlabel("no('HI')")	
plt.ylabel("no('HELLO')")
plt.bar	(total_hi_list[1],total_hello_list[1],color='r')
plt.show()

	



