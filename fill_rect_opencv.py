#!/usr/bin/env python3


#IMPORT MODULES
import cv2

#READING IMAGE
img_goku=cv2.imread('/home/priyank/Desktop/hhh.jpeg',1)		#CHANGE THE PATH
img_vegeta=cv2.imread('/home/priyank/Desktop/vegeta.jpeg',1)	#CHANGE THE PATH


#SELECTING FRAME TO REPLACE WITH NEW IMAGE

#cv2.line(img,(0,0),(194,259),(255,255,255),10)
cv2.rectangle(img_goku,(50,35),(160,175),(255,255,255),3)
new_goku=img_goku[35:175,50:160]

cv2.rectangle(img_vegeta,(85,0),(195,140),(255,255,255),3)
img_vegeta[0:140,85:195]=new_goku



print(img_vegeta.shape)
print(new_goku.shape)


#SHOWING IMAGE
cv2.imshow('goku',new_goku)
cv2.imshow('vegeta',img_vegeta)
cv2.waitKey(0)

#DESTROYING THE IMAGE WINDOW
cv2.destroyAllWindows()

#168, 299 vegeta
#140, 110 goku
