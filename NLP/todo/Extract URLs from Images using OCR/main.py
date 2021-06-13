from PIL import Image
import pytesseract
import cv2
import re
import os
import webbrowser


img=cv2.imread('Testing.png')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# file="{}.png".format(os.getpid())
# cv2.imwrite(file,gray)

# text=pytesseract.image_to_string(Image.open(gray))

text=pytesseract.image_to_string(gray)

# texts=text.replace("\n","").split(" ")

print(text)

urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[.]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', "text  https://www.youtube.com/channel/UC5hHNks012Ca2o_MPLRUuJw/videos ")
emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)
phoneNums=re.findall("^([+]|[9][1]|[0])([0-9]{10})+","+91711478159715 llol")


print(phoneNums)
# print(text.replace("\n",""))
# print(text.replace("\n",""))

# urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[.]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
# regex = '^[A-Za-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# mail=re.search(regex,text)


# print(mail)

# print(text)



