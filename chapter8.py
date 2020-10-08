#!/usr/bin/env python
#
# find shapes, count them up by type and their areas.

import cv2
import numpy as np
from util.display import stackImages
from util.edge_detection import getContours
from util.edge_detection import detectShape
from model.shape import Shape

path = 'resources/shapes.png'
img = cv2.imread(path)

# convert to grayscale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
print(f"gray: {imgGray.shape}, blur: {imgBlur.shape}")

# begin finding edges.  Canny maybe go into image detection
imgCanny = cv2.Canny(imgBlur,50,50)
imgBlank = np.zeros_like(img)
imgStack = stackImages(0.6,(
    [img,imgGray,imgBlur],
    [imgCanny,imgBlank,imgBlank]))

print(f"stack: {imgStack.shape}")

# Using the canny image (image with edges), detect closed contours
contours = getContours(imgCanny)
shapes = []
for cnt in contours:
  shape = detectShape(cnt)
  shapes.append(shape)
  print(f"shape: {shape.toString()}")





