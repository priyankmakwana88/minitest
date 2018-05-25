#!/usr/bin/env python

#IMPORT LIBRARIES
import socket
#import netifaces as ni
import thread

#AUTO DETECT SYSTEM IP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="127.0.0.1"
port=8870

#BINDING IP AND PORT
s.bind(	(ip,port))


#INITIAL SEND
data_rec=s.recvfrom(1000)
msg_rec=data_rec[0]
dest_add=data_rec[1]
print (msg_rec)

#RECEIVER FUNCTION
def receive_msg():
	while 1:
		print("Received Message : "),
		data_rec=s.recvfrom(1000)
		msg_rec=data_rec[0]
		print (msg_rec)


#SENDER FUNCTION
def send_msg():
	while 1:
		reply=raw_input("Enter your Message : ")
		#s.sendto(reply,(data_rec[1]))
		s.sendto(reply,(dest_add))


thread.start_new_thread(send_msg,())
thread.start_new_thread(receive_msg,())

while 1:
	pass

