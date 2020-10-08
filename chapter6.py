#!/usr/bin/env python

import cv2
import numpy as np

img = cv2.imread('resources/lena_color.jpg')

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

print(f"single image: {img.shape}")
print(f"horizontal stack: {imgHor.shape}")
print(f"vertical stack: {imgVer.shape}")

#cv2.show(imgHor)
#cv2.wait(0)

# This only works if both images are of the same type & color channel (same dim)
# Also, hard to add images afterwards

# so, we need some helper funtions!
#https://github.com/murtazahassan/OpenCV-Python-Tutorials-and-Projects
# basics, joining_multiple_images-to-display

# with stackImages, you can have grayscale with rgb



