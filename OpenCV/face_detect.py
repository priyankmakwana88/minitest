#!/usr/bin/env python3

##CHECK THE EDIT(INCOMPLETE)

##TOO MUCH COMPLEXITY REAL TIME (SLOW)





#IMPORT LIBRARIES
import cv2
import numpy as np

#INITIALIZING WEBCAM
cam=cv2.VideoCapture(0) #change to '1' if external webcam is attached along with internal


#KEEP CAMERA RUNNING UNTIL 'q' IS PRESSED
while cam.isOpened():
	status,frame=cam.read()
	red=cv2.inRange(frame,(65,45,45),(83,60,60))
	shape=red.shape
	row=int(shape[0])
	col=int(shape[1])
	
	#MY APPROACH (SLOW AT RUNTIME)	
	'''	
	fr=[]
	fc=[]
	for i in range(0,row):
		for j in range(0,col):
			if red[i][j]==255:
				fr.append(i) 
				fc.append(j)
	fr=sorted(fr)
	fc=sorted(fc)
	'''

	#USING FUNCTIONS
	color_find=np.where(red==255)
	#print(color_find)
	#color_find[0]
	print(color_find[0].tolist())	
	#st_pt=(np.min(color_find[1]),np.min(color_find[0]))
	#end_pt=(np.max(color_find[1]),np.max(color_find[0]))
	#cv2.rectangle(frame,st_pt,end_pt,(255,255,255),4)
	cv2.imshow('cam0',red)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
cam.release()

