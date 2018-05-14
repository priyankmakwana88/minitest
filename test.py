#!/usr/bin/python
#i=0
#q=()
#for i in (0,1,2,3,4):
print "Enter 5 characters of a tuple  : \n"
x1 = raw_input()
x2 = raw_input()
x3 = raw_input()
x4 = raw_input()
x5 = raw_input()
	
q=(x1,x2,x3,x4,x5)
print
for i in (0,1,2,3,4):
	r=q[i].find("ll")
	if(r>=0):
		print "Position of 'll' in ",q[i]," is = ",r 
	else:
		print "NOT FOUND !!"

