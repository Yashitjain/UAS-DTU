import cv2
import numpy as np

def nothing(x):
    pass

i=1
for i in range(1,11): 
    
    img=cv2.imread(str(i)+".png")
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    l_bgrass=np.array([35,0,0])
    u_bgrass=np.array([119,255,255])

    l_burnt=np.array([1,0,0])
    u_burnt=np.array([32,255,255])

    mask_unburnt=cv2.inRange(hsv,l_bgrass,u_bgrass)   
    mask_burnt=cv2.inRange(hsv,l_burnt,u_burnt)

    res = cv2.bitwise_and(img,img,mask=mask_unburnt)

    img[mask_unburnt>0]=(235,206,135)
    img[mask_burnt>0]=(0,255,255)

    cv2.imshow("img"+str(i),img)
    cv2.waitKey(0)
        
