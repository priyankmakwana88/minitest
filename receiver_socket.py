#!/usr/bin/env python3

import socket

recv_ip='192.168.0.108'
port=8888


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((recv_ip,port))

while 1:
	print (s.recvfrom(1000))

