#!/usr/bin/env python

import socket


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="192.168.43.253"
port=9999


while 1:

	msg=input()
	#s.sendto(bytes(10),("192.168.43.253",9999))
	s.sendto(msg,(ip,port))

