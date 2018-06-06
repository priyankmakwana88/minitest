#!/usr/bin/env python3

#IMPRTING LIBRARIES
import cv2
import numpy as np

cat1=cv2.imread('cat1.jpg',1)
cat2=cv2.imread('cat2.jpg',1)
cat3=cv2.imread('cat3.jpg',1)
cat4=cv2.imread('cat4.jpg',1)
cat5=cv2.imread('cat5.jpg',1)

cat=[cat1,cat2,cat3,cat4,cat5]

for i in range(0,len(cat)):
	heigth=cat[i].shape[0]
	width=cat[i].shape[1]
	bgr=cat[i].shape[2]
	
	factor=width*bgr
	cat[i]=cat[i].reshape(heigth,factor)
	np.savetxt('cat'+str(i+1)+'.txt',cat[i],fmt='%d',comments='reshaped data')

