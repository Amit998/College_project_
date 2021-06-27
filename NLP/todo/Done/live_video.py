import cv2
import numpy as np
import pytesseract
import time
import asyncio
import cvzone
import cv2


myclassifier=cvzone.Classifier('model/keras_model.h5','model/labels.txt')
fpsReader=cvzone.FPS()

class live_text:
    min_value=2
    temp_st={

    }

    color = (20, 20, 20)
    predictions_dictonary={
        0:"Readable",
        1 :"RoadSign",
        2 :"Id",
        3 :"BookCover"
    }

    def __init__(self):
        pass

    def validate_image(self,img):
        laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()
        print(laplacian_var)
        if laplacian_var < 5:
            return False
        else:
            return True
    def classify(self,image):
        predictions,index=myclassifier.getPrediction(image,scale=1)
        prediction_name=self.predictions_dictonary[index]
        return predictions,index,prediction_name
    
    def mapper(self,h):
        h = h.reshape((4,2))
        
        hnew = np.zeros((4,2),dtype = np.float32)
        add = h.sum(1)
        
        hnew[0] = h[np.argmin(add)]
        hnew[2] = h[np.argmax(add)]
        diff = np.diff(h,axis = 1)
        hnew[1] = h[np.argmin(diff)]
        hnew[3] = h[np.argmax(diff)]
        return hnew
    async def get_prespectiveImage(self,approx):
        pts=np.float32([[0,0],[800,0],[800,800],[0,800]])
        op=cv2.getPerspectiveTransform(approx,pts)
        self.dst=cv2.warpPerspective(self.image,op,(800,800))

        return self.dst

    async def detect_text(self,image):
        # if self.image_process_flag == 0 :self.image_preprocess()

        self.text=pytesseract.image_to_string(image)

        self.text=self.text.replace(','," ")
        self.text=self.text.replace('\n'," ")
        self.text=self.text.replace('\\'," ")
        self.text=self.text.replace('  '," ")
        self.text_detection_flag=1
        # self.text=self.text.split(" ")

        if (self.text == None):
            print('empty')
            return
        else:
            length=len(self.text.split(" "))
            text=self.text
            if ( length not in self.temp_st.keys and length > self.min_value):
                self.temp_str[length]=self.text
                self.min_value=length

            return self.text
        

    def image_preprocess(self,img):
        self.image=img

        if(self.validate_image(img) != True):
            print('Please take image again')
            return
        orig=img.copy()
        gray=cv2.cvtColor(orig,cv2.COLOR_BGR2GRAY)
        blurred=cv2.GaussianBlur(gray,(5,5),0)
        edge=cv2.Canny(blurred,30,50)
        contours,hierarchy=cv2.findContours(edge,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        contours=sorted(contours,key=cv2.contourArea,reverse=True)
        for c in contours:
            p=cv2.arcLength(c,True)
            approx=cv2.approxPolyDP(c,0.02*p,True)

            if (len(approx) == 4):
                self.target=approx
                break
        approx=self.mapper(self.target)
        

        return approx
    
    async def live_image(self):
        vid = cv2.VideoCapture(0)
        while True:
            _,img=vid.read()
            img=cv2.resize(img,(800,800))
            approx=self.image_preprocess(img)
            start_point = (int(approx[0][0]), int(approx[0][1]))
            end_point = (int(approx[2][0]), int(approx[2][1]))
            img=cv2.rectangle(img,start_point,end_point,self.color,3)

            dst=await self.get_prespectiveImage(approx)

            text=await self.detect_text(dst)
            #print(text)

            _,__,prediction2=self.classify(dst)
            _,__,prediction1=self.classify(img)
            print(prediction2,prediction1)

            cv2.imshow("dst",dst)
            cv2.imshow("Frame",img)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        img.release()
        cv2.destroyAllWindows()


    def test(self):
        asyncio.run(self.live_image())
       
    
lt=live_text()
lt.test()
