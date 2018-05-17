#!/usr/bin/env python

import socket


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="127.0.0.1"
port=8888


while 1:
	msg=raw_input("Enter message to send : ")
	s.sendto(msg,(ip,port))
	rec_data=s.recvfrom(1000)
	print(rec_data[0])
