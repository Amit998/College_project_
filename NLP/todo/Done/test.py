import cvzone
import cv2

cap=cv2.VideoCapture(0)


myclassifier=cvzone.Classifier('model/keras_model.h5','model/labels.txt')
fpsReader=cvzone.FPS()

predictions_dictonary={
    0:"Readable",
    1 :"RoadSign",
    2 :"Id",
    3 :"BookCover"
}

def classify(image):
    predictions,index=myclassifier.getPrediction(image,scale=1)
    prediction_name=predictions_dictonary[index]
    return predictions,index,prediction_name

while True:
    _,img=cap.read()
    prediction,index=classify(img)
    print(predictions_dictonary[index])



    cv2.imshow("image",img)
    cv2.waitKey(1)




