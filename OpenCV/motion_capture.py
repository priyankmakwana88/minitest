#!/usr/bin/env python3

import cv2

cam=cv2.VideoCapture(0)

def image_diff(img1,img2,img3):
	diff1=cv2.absdiff(img1,img2)
	diff2=cv2.absdiff(img2,img3)
	img=cv2.bitwise_and(diff1,diff2)
	return img
	

im1=cam.read()[1]
im2=cam.read()[1]
im3=cam.read()[1]

gray1=cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(im2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(im3,cv2.COLOR_BGR2GRAY)

gray1=cv2.GaussianBlur(gray1, (21, 21), 0)
gray2=cv2.GaussianBlur(gray2, (21, 21), 0)
gray3=cv2.GaussianBlur(gray3, (21, 21), 0)

while 1:
	new_img=image_diff(gray1,gray2,gray3)
	thresh = cv2.threshold(new_img, 18, 255, cv2.THRESH_BINARY)[1]	#min-25
	#thresh = cv2.dilate(thresh, None, iterations=1)		#iteration-2
	cv2.imshow('motion',thresh)
	
	status,frame=cam.read()
	gray1=gray2
	gray2=gray3
	gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cv2.destroyAllWindows()
cam.release()
