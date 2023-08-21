import numpy as np
import cv2 as cv
def contours_func(img):
    hsvimg=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    
    maskr=cv.inRange(hsvimg,(0,0,0),(0,255,255))
    maskb=cv.inRange(hsvimg,(2,0,255),(179,255,255))

    diffred=cv.bitwise_and(img,img,mask=maskr)
    diffredgray=cv.cvtColor(diffred,cv.COLOR_BGR2GRAY)

    diffblue=cv.bitwise_and(img,img,mask=maskb)
    diffbluegray=cv.cvtColor(diffblue,cv.COLOR_BGR2GRAY)
    
    blurred=cv.GaussianBlur(diffredgray,(5,5),0)
    _,threshred=cv.threshold(blurred,70,255,cv.THRESH_BINARY)

    blurblue=cv.GaussianBlur(diffbluegray,(5,5),0)
    _,threshblue=cv.threshold(blurblue,25,255,cv.THRESH_BINARY)

    contoursred,_=cv.findContours(threshred,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    contoursblue,_=cv.findContours(threshblue,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    
    return [len(contoursred),len(contoursblue)]

