#!/usr/bin/env python

import cv2
import numpy as np

img = cv2.imread("resources/lena.jpg")

# convert to grayscale
imgGray = cv2.cvtColor(img, COLOR_BGR2GRAY)
cv2.imshow("Gray Image", imgGray)
cv2.waitKey(2)

# blur image - kernel has to be odd numbers
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Blur Image", imgBlur)
cv2.waitKey(2)

# img edge detection
imgCanny = cv2.Canny(img, 150, 150)
cv2.imshow("Canny Image", imgCanny)
cv2.waitKey(2)

# kernel is a matrix - the space of operations.  Here, the dialation function will thicken detected lines.  The workspace is then 5x5
kernel = np.ones((5,5),np.uint8)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
cv2.imshow("Dialation Image", imgDialation)
cv2.waitKey(2)

# opposite of dialation is erosion
imgEroded = cv2.erod(imgDialation, kernel, iterations=1)
cv2.imshow("Erosion Image", imgEroded)
cv2.waitKey(2)




