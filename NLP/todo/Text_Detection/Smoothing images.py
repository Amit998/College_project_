import cv2
import numpy as np

img=cv2.imread("image/5.png")

averaging=cv2.blur(img,(5,5))
gaussian=cv2.GaussianBlur(img,(5,5),0)



cv2.imshow("original",img)
cv2.imshow("avg",averaging)
cv2.imshow("gaussian",gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()