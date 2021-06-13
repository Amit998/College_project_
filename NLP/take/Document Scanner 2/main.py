import cv2
import numpy as np
import pytesseract


image=cv2.imread('image/3.jpg')
image=cv2.resize(image,(1300,800))

orig=image.copy()

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# cv2.imshow("Title",gray)
# cv2.waitKey(0)


blurred=cv2.GaussianBlur(gray,(5,5),0)
# cv2.imshow("gaussianBlur",blurred)
# cv2.waitKey(0)


edge=cv2.Canny(blurred,30,50)
cv2.imshow('edge',edge)
# cv2.waitKey(0)

contours,hierarchy=cv2.findContours(edge,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
contours=sorted(contours,key=cv2.contourArea,reverse=True)


target=None

for c in contours:
    p=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.02*p,True)

    if (len(approx) == 4):
        target=approx
        break



print(target)

import mapper

approx=mapper.mapp(target)

pts=np.float32([[0,0],[800,0],[800,800],[0,800]])


op=cv2.getPerspectiveTransform(approx,pts)
dst=cv2.warpPerspective(orig,op,(800,800))


text=pytesseract.image_to_string(dst)
print(text)

cv2.imshow("final",dst)
cv2.waitKey(0)
