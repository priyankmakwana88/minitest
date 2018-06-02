#!/usr/bin/env python3

#IMPORTING LIBRARIES
import cv2

#SETUP WEBCAM
cam=cv2.VideoCapture(0)

#CAPTURE SHORT IMAGE BURST UNTIL 'q' IS PRESSED
i=0
while cam.isOpened():
	status,frame=cam.read()
	cv2.imwrite(str(i)+'.jpeg',frame)
	cv2.imshow('hi',frame)
	if cv2.waitKey(1) & 0xFF== ord('q'):
		break
	i=i+1
cv2.destroyAllWindows()
cam.release()


#READING SAVEED IMAGES 
nimg=[]
for k in range(0,i):
	x=cv2.imread(str(k)+'.jpeg',1)
	nimg.append(x)

#DISPLAYING IMAGES CAPTURED UNTIL 'q' IS PRESSED
l=len(nimg)
j=0
while 1:
	cv2.imshow('hi',nimg[j])
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	j=j+1
	if j>=l:
		j=0

cv2.destroyAllWindows()
