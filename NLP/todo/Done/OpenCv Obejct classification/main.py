import cvzone
import cv2

cap=cv2.VideoCapture(0)


myclassifier=cvzone.Classifier('myModel/keras_model.h5','myModel/labels.txt')
fpsReader=cvzone.FPS()


while True:
    _,img=cap.read()
    predictions,index=myclassifier.getPrediction(img,scale=1)
    print(predictions,index)
    fps,img=fpsReader.update(img,pos=(20,100))
    print(fps)


    cv2.imshow("image",img)
    cv2.waitKey(1)