#!/usr/bin/env python3

import cv2
import numpy as np

#READING THE IMAGE
path=input('Enter the path of image : ')
img=cv2.imread(path,1)

dim=input('Enter the dimensions to distribute : ')
w=dim.split()[0]
h=dim.split()[-1]

w1=h
h1=w
#print (w,h)

shape=img.shape
imgh=shape[0]
imgw=shape[1]

#FOR VERTICAL CHECK
countx=0
county=0

i=0
while i<=imgw:
	countx=countx+1
	i=i+int(w)

j=0
while j<=imgh:
	county=county+1
	j=j+int(h)

total1=countx*county

#FOR HORIZONTAL CHECK
countx1=0
county1=0

i1=0
while i1<=imgw:
	countx1=countx1+1
	i1=i1+int(w1)

j1=0
while j1<=imgh:
	county1=county1+1
	j1=j1+int(h1)

total2=countx1*county1

w=int(w)
h=int(h)
data=img[0:int(h),0:int(w)]
#print(shape)
#print (w,h)
#print (w1,h1)
#print(total1,total2)

'''
new_img=img
if total1>total2:

	x1=0
	x2=int(h)
	y1=0
	y2=int(w)	
	while total1>0:
		new_img[x1:x2,y1:y2]=data
		if x2>=imgh:
			x1=0
			x2=w
			y1=y2
			y2=y2+w
		if y2>=imgw:
			break
		x1=x2
		x2=x2+h
		
		
		total1=total1-1
	cv2.imshow('new',new_img)
	cv2.imshow('original',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
'''
print(total1)
#CUT THE IMAGES
cut=[]
p0=0
p1=0
a0=h
a1=w
if total1>total2:
	print("t1",total1)
	while total1>0:
		nimg=img[p0:a0,p1:a1]
		#print(type(nimg))
		#nimg=nimg.tolist()
		#print(type(nimg))
		cut.append(nimg)
		
		p1=a1
		a1=a1+w
		if a1==countx:
			a1=w
			p0=a0
			a0=a0+h
			p1=0
		if a0==county:
			break
		total1=total1-1

print(total1)
#print(np.shape(cut))


#cv2.imshow('a',cut[0])
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#DISPLAYING IMAGES CAPTURED UNTIL 'q' IS PRESSED
#l=len(cut)

#print(l)
j=0
for i in cut:
	
	cv2.imshow(str(j),i)
	cv2.waitKey(0)
	j=j+1
cv2.destroyAllWindows()
