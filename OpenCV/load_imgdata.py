#!/usr/bin/env python3

import cv2
import numpy as np

cat1=np.load('cat1.npy')
shape=cat1.shape
#(x,y) ---> cat1 read
#x=shape[0]
#y=shape[1]
#a=cv2.imread('cat1.jpg',1)
#(x,y1,z1)--->cat1 image data orig.
#y1=int(y/3)
#z1=3

#print(x,y1,z1)
#cat1=cat1.reshape(x,y1,z1)

#if np.array_equal(a,cat1):
#	print('hiiiiii')

cv2.imshow('cat',cat1)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(cat1)
print(cat1.shape)
#print(a)
