#!/usr/bin/python

#print "Enter : "
#x=raw_input()
print "Enter 5 characters of a tuple  : \n"
x1 = raw_input()
x2 = raw_input()
x3 = raw_input()
x4 = raw_input()
x5 = raw_input()
	
q=(x1,x2,x3,x4,x5)
print
for i in (0,1,2,3,4):
	#r=q[i].find("ll")d 
	#if(r>=0):
	#	print "Position of 'll' in ",q[i]," is = ",r 
	#else:
	#	print "NOT FOUND !!"
	if 'll' in q[i]:
		pos=-1
		#j=0
		l=len(q[i])
		print ""
		print "Position of 'll' in ",q[i]," is ",
		while pos < l:
			pos=q[i].find("ll",pos+1)
			if pos<0:
				break		
			print pos,	
			#pos=pos+1
	else:
		print ""
		print "'ll' in ",q[i], " is NOT FOUND!"	
