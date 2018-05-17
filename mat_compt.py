#!/usr/bin/env python3

import numpy as np
import math

#CREATING ARRAY
data_list=np.array([])
available_row=np.array([])
available_col=np.array([])

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
		print("CURRENT STATUS -> ** COMPATIBLE **")
		break

#CALCULATING AVAILABLE DIMENSIONS
size=len(data_list)
print("\nAvailable dimensions are : ")
for i in range(2,size-1):
	if (size%i)==0:
		print (i,"x",int(size/i)) 
		available_row=np.append(available_row,i)
		available_col=np.append(available_col,int(size/i))


#TYPE CONVERSION
available_row=available_row.astype(int)
available_col=available_col.astype(int)

list_row=available_row.tolist()
list_col=available_col.tolist()

new_list=data_list.astype(int)

#FORMING THE MATRIX
print("Enter the dimensions (n x m) from the list above: ")
row=int(input("n : "))
column=int(input("m : "))

print(type(row))

if not((row in list_row) or (column in list_col) ):
	print("Enter valid data!!")
	row=input("n : ")
	column=input("m : ")

new_list=np.reshape(new_list,(row,column))


print(new_list)
