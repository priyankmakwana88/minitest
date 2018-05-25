#!/usr/bin/env python

import socket
import thread
import netifaces


#ip=netifaces.ifaddresses("wlp9s0")[netifaces.AF_INET][0]['addr']
#ip =ni.ifaddresses("eth0")[ni.AF_INET][0]['addr']
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="127.0.0.1"
port=8870

#s.bind((ip,port)) #CHECK

#FUNCTION TO SEND THE DATA
def send_msg():
	while 1:
		msg=raw_input("Enter message to send : ")
		s.sendto(msg,(ip,port))


#FUNCTION TO RECEIVE THE MESSAGE
def receive_msg():
	while 1:
		rec_data=s.recvfrom(1000)
		print("Message Received : ",rec_data[0])

thread.start_new_thread(send_msg,())
thread.start_new_thread(receive_msg,())

while 1:
	pass

