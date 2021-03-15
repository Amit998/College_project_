import pytesseract
import cv2
import matplotlib.pyplot as plt


import pyttsx3
engine = pyttsx3.init()

pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

# img=cv2.imread('img/test3.jpg')

img=cv2.imread('test1.jpg')

# plt.imshow(img)
# plt.show()

img2Char=pytesseract.image_to_string(img)
# print(img2Char)

img_box=pytesseract.image_to_boxes(img)
# print(img_box)
imgH,imgW,_=img.shape
# print(imgH,imgW)

for boxes in img_box.splitlines():
    boxes=boxes.split(' ')
    x,y,w,h=int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
    cv2.rectangle(img,(x,imgH-y),(w,imgH-h),(0,0,255),3)

# plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
# plt.show()

print(img2Char)
# engine.say(img2Char)
# engine.runAndWait()
