#!/usr/bin/env python

import cv2
print("Package imported")

# import an image
img = cv2.imread("resources/lena_color.jpg")
cv2.imshow("Output",img)
#cv2.waitKey(0)

# import a video
cap = cv2.VideoCapture("resources/test_video.mp4")

while True:
    success, img_vid = cap.read()
    cv2.imshow("Video", img_vid)
    # plays video until q key pressed or end of video
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

# use webcam feed
cam_cap = cv2.VideoCapture(0)
cam_cap.set(3,640) # set width
cam_cap.set(4,480) # set height
cam_cap.set(10,100) # change brightness

while True:
    success, img_vid = cap.read()
    cv2.imshow("Video", img_vid)
    # plays video until q key pressed or end of video
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
