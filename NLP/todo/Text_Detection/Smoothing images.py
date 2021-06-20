import cv2
import numpy as np

img=cv2.imread("image/noisy4.png")
# img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# _,result=cv2.threshold(img,35,255,cv2.THRESH_BINARY)

# adaptive=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,101,2)


# cv2.imshow("img",adaptive)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


averaging=cv2.blur(img,(5,5))
gaussian=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img,5)
bilateral=cv2.bilateralFilter(img,5,75,75)


# cv2.imshow("original",img)
# cv2.imshow("avg",averaging)
# cv2.imshow("gaussian",gaussian)

# cv2.imshow('median',median)
# cv2.imshow('bilateral',bilateral)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



#SHARPE IMAGE

image_data=cv2.imread('image/balloons_noisy.png')
image_data=cv2.resize(image_data,(400,400))
sharpening_filter=np.array([[-1,-1,-1],
                            [-1,9,-1],
                            [-1,-1,-1]])      

sharpened_image=cv2.filter2D(image_data,-1,sharpening_filter)


cv2.imshow('image show',sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()