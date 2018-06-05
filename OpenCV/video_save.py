#!/usr/bin/env python3

#IMPORT LIBRARIES
import cv2

#INITIALIZING CAMERA
cam=cv2.VideoCapture(0)

#DETECT CAMERA FRAME SIZE
cam_width=int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
cam_height=int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

#FINDING VIDEO FORMAT TO SAVE
video_format=cv2.VideoWriter_fourcc(*'XVID')
#print(video_format)

video=cv2.VideoWriter('pri.avi',video_format,10.0,(cam_width,cam_height))


while cam.isOpened:
	status,frame=cam.read()
	cv2.imshow('me',frame)
	video.write(frame)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
cv2.destroyAllWindows()
cv2.release()

