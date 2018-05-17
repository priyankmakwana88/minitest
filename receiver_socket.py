#!/usr/bin/env python

import socket
import netifaces as ni


recv_ip=ni.ifaddresses("wlp9s0")[ni.AF_INET][0]['addr']
#recv_ip =ni.ifaddresses("eth0")[ni.AF_INET][0]['addr']


port=8888


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((recv_ip,port))

while 1:
	data_rec=s.recvfrom(1000)
	msg_rec=data_rec[0]
	print (msg_rec)
	reply=raw_input("Enter your reply : ")
	s.sendto(reply,(data_rec[1]))
