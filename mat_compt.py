#!/usr/bin/env python3

import numpy as np
import math

#CREATING ARRAY
data_list=np.array([])

print("Enter elements for matrix (press 'q' if done) : ")

#TAKING INPUT
while 1:
	data=input()
	if data == 'q' or data == 'Q':
		break
	data_list=np.append(data_list,data)
	
size=len(data_list)

#CHECKING MATRIX COMPATIBLITY
for i in range(2,int(math.sqrt(size)+1)):
	if not((size%i) == 0) :
		print("CURRENT STATUS -> NOT COMPATIBLE!!")
		print("Enter one more element")
		data=input()
		data_list=np.append(data_list,data)
		break

#CALCULATING AVAILABLE DIMENSIONS
print("\nAvailable dimensions are : ")
for i in range(2,size-1):
	if (size%i)==0:
		print (i,"x",int(size/i)) 
