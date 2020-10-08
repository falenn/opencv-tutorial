#!/usr/bin/env python

import cv2
import numpy as np

# create an empty (black) color (RGB) image
img = np.zeros((512,512,3),np.uint8) 
cv2.imshow("Image", img)
print(img.shape)

# color just part of the image
img[200:300, 100:300] = 255, 0, 0
cv2.imshow("Image", img)
cv2.waitKey(2)

# color the whole matrix blue
img[:] = 255,0,0
cv2.imshow("Image", img)
cv2.waitKey(2)

# draw a line
cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.imshow("Image", img)
cv2.waitKey(2)

# reset
img[:] = 255,0,0
cv2.imshow("Image", img)
cv2.waitKey(2)

# draw a line diagonal across the whole image
# get width and hieght from shape output to set extents
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.imshow("Image", img)
cv2.waitKey(2)

# draw rectangle
# start, end, color, thickness
cv2.rectangle(img(0,0),(250,350)(0,0,255),2)
cv2.imshow("Image", img)
cv2.waitKey(2)

# fill a shape
cv2.rectangle(img(0,0),(250,350)(0,0,255),cv2.FILLED)
cv2.imshow("Image", img)
cv2.waitKey(2)

# draw cirlce
img[:] = 255,0,0
cv2.circle(img, (400,50),30,(255,255,0),5)
cv2.imshow("Image", img)
cv2.waitKey(2)

# display text
# text, starting loc, font, scale, color, 
img[:] = 255,0,0
cv2.putText(img," OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
cv2.imshow("Image", img)
cv2.waitKey(2)


