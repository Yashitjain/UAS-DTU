import contours as cont
import obj_detection as objdet
import cv2
list=[]
for i in range(1,11):
    img=cv2.imread(str(i)+".png")
    sub_list=cont.contours_func(img)
    objdet.roi(img) 
    list.append(sub_list)
print(list) 