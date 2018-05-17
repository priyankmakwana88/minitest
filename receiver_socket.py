#!/usr/bin/env python

import socket

recv_ip='127.0.0.1'
port=8888


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((recv_ip,port))

while 1:
	data_rec=s.recvfrom(1000)
	msg_rec=data_rec[0]
	print (msg_rec)
	reply=raw_input("Enter your reply : ")
	s.sendto(reply,(data_rec[1]))
