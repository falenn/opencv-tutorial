#!/usr/bin/env python

import cv2
import numpy as np

# we are resizing images here
# coordinate system starts top-left corner

img = cv2.imread("resources/lena_color.jpg")
print(img.shape)

# resize width / height
imgResize = cv2.resize(img, (300,200))
print(imgResize.shape)

# img cropping
# since image is just a matrix of nums, we can just operate on the image using numpy
# hieght, then width - its a matrix
imgCropped = img[0:200, 200:500]
print(imgCropped.shape)


