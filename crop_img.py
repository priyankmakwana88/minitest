#!/usr/bin/env python3

#IMPORTING LIBRARIES
import cv2
import numpy as np


#READING IMAGE FROM USER AND FINDING ITS DIMENSION
img_path=input("Enter the file path : ")
img=cv2.imread(img_path,1)
shape=img.shape
img_height=shape[0]
img_width=shape[1]



#ASKING THE OPTIONS
option='''
1: Crop the image into HALF(1/2)
2: Crop the image into QUARTER(1/4)
3: Crop the image into ONE-EIGHTH(1/8)
'''

#FUNCTIONS
def half():
	img_h=int(img_height/2)
	img_w=int(img_width/2)
	img1=img[0:img_h,0:img_w]
	cv2.imshow('cropped',img1)
	
	zero=np.zeros((img_h,img_w,3))
	img[0:img_h,0:img_w]=zero
	img2=img
	
	cv2.imshow('rest',img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
		
def quarter():
	img_h=int(img_height/4)
	img_w=int(img_width/4)
	img1=img[0:img_h,0:img_w]
	cv2.imshow('cropped',img1)

	zero=np.zeros((img_h,img_w,3))
	img[0:img_h,0:img_w]=zero
	img2=img
	
	cv2.imshow('rest',img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

'''
def eighth():
	img_h=int(img_height/8)
	img_w=int(img_width/8)
	img1=img[0:img_h,0:img_w]
	cv2.imshow('cropped',img1)

	zero=np.zeros((img_h,img_w,3))
	img[0:img_h,0:img_w]=zero
	img2=img

	cv2.imshow('rest',img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
'''

print(option)
choice=input('\nEnter your choice : ')

#ITERATING THROUGH CHOICES
if choice=='1':
	half()
elif choice=='2':
	quarter()
#elif choice=='3':
#	eighth()

