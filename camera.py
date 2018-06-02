#!/usr/bin/env python3

#IMPORT LIBRARIES
import cv2

#INITIALIZING WEBCAM
cam=cv2.VideoCapture(0) #change to '1' if external webcam is attached along with internal


#KEEP CAMERA RUNNING UNTIL 'q' IS PRESSED
while cam.isOpened():
	status,frame=cam.read()
	new=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('cam0',frame)
	cv2.imshow('cam1',new)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
cam.release()

