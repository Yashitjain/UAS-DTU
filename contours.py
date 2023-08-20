import numpy as np
import cv2 as cv
def contours_func(img):
    # img = cv.imread('1.png')
    # imgcopy=cv.imread("1.png")

    hsvimg=cv.cvtColor(img,cv.COLOR_BGR2HSV)

    maskr=cv.inRange(hsvimg,(0,0,0),(0,255,255))
    maskb=cv.inRange(hsvimg,(2,0,255),(179,255,255))

    diffred=cv.bitwise_and(img,img,mask=maskr)
    diffredgray=cv.cvtColor(diffred,cv.COLOR_BGR2GRAY)
    # cv.imshow("diffredgray",diffredgray)

    diffblue=cv.bitwise_and(img,img,mask=maskb)
    diffbluegray=cv.cvtColor(diffblue,cv.COLOR_BGR2GRAY)
    # cv.imshow("diffbluegray",diffbluegray)


    blurred=cv.GaussianBlur(diffredgray,(5,5),0)
    _,threshred=cv.threshold(blurred,70,255,cv.THRESH_BINARY)

    blurblue=cv.GaussianBlur(diffbluegray,(5,5),0)
    _,threshblue=cv.threshold(blurblue,25,255,cv.THRESH_BINARY)


    contoursred,_=cv.findContours(threshred,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    contoursblue,_=cv.findContours(threshblue,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

    # print(len(contoursred))
    # print(len(contoursblue))

    # cv.drawContours(diffred,contoursred,-1,(255,255,255),4)
    # cv.drawContours(diffblue,contoursblue,-1,(255,255,255),4)

    # cv.imshow("diffred",diffred)
    # cv.imshow("diffblue",diffblue)

    # cv.waitKey(0)

    return [len(contoursred),len(contoursblue)]

