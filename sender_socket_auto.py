#!/usr/bin/env python

import socket
import netifaces as ni



#ip =ni.ifaddresses("eth0")[ni.AF_INET][0]['addr']


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=ni.ifaddresses("wlp9s0")[ni.AF_INET][0]['addr']
#ip="127.0.0.1"
port=8888


while 1:
	
	s.sendto(raw_input("Enter message to send : "),(ip,port))
	
