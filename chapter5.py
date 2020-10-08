#!/usr/bin/env python

import cv2
import numpy as np

# trying to warp perspective
img = cv2.imread("resources/1280px-7_playing_cards.jpg")
print(img.shape)

width,height = 250,350

# using MS paint, we have selected the 4 corners of the top playing card
pts1 = np.float32([[928,246],[1174,457],[617,567],[886,802]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))

print("Result of transform")
print(imgOutput.shape)


