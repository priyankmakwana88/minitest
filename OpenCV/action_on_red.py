#!/usr/bin/env python3

##INCOMPLETE

#IMPORT LIBRARIES
import cv2
import numpy as np

#INIT. CAM
cam=cv2.VideoCapture(0)

while cam.isOpened():
	status,frame=cam.read()
	white_frame=cv2.inRange(frame,(255,255,255),(255,255,255))
	print(type(white_frame))	
	
	if np.where(white_frame==255)[][]
	cv2.imshow('live',white_frame)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
	

cv2.destroyAllWindows()
cam.release()

