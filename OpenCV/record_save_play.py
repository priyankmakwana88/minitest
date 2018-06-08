#!/usr/bin/env python3

#IMPRTING LIBRARIES
import cv2
import numpy as np

cam=cv2.VideoCapture(0)

i=0
while cam.isOpened():
	status,frame=cam.read()
	cv2.imshow('live',frame)
	np.save('frame'+str(i),frame)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
	i=i+1

for j in range(0,i):
	img=np.load('frame'+str(j)+'.npy')
	cv2.imshow('captured',img)
	if cv2.waitKey(100) & 0xFF==ord('q'):
		break
	if j==i-1:
		j=0

cv2.destroyAllWindows()
cam.release()
