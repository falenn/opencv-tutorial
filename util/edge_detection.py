# Image processing for edge detection

import cv2
import numpy as np
from model.shape import Shape

MIN_AREA=100

def getContours(img):
    # retreive extreme outer contours (outer corners)
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours

def detectShape(contour):
    shape = Shape()
    
    shape.area = cv2.contourArea(contour)
    #print(f"Area: {shape.area}, for cont: {contour}")
    if shape.area> MIN_AREA:
        shape.perimeter = cv2.arcLength(contour,True)
        approx = cv2.approxPolyDP(contour, 0.02*shape.perimeter, True)
        #print(f"approx corners: {approx}, {len(approx)}")

        # this is where we approx the type of shape
        objCor = len(approx)

        # bounding box around the approx
        x,y,w,h = cv2.boundingRect(approx)
        shape.boundingBox = [x,y,w,h]
        # from the bounding box, we can get center-point, max width, height

        if objCor ==3:objectType = "Tri"
        elif objCor ==4:
            aspRatio = w/float(h)
            if aspRatio >0.95 and aspRatio < 1.05: objectType = "Square"
            else:objectType = "Rect"
        elif objCor >4: objectType = "Circle"
        else: objectType = "None"

        #print(f"Obj Type: {objectType}")
        shape.type=objectType
        shape.corners=objCor

    else:
        shape.perimeter =0
    return shape

