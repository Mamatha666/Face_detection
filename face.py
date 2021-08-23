import numpy
import cv2

img=cv2.imread(r'C:\Users\Mamatha\Desktop\Major project\neural.jpg')
cv2.imshow('image',img)
 



detect=cv2.CascadeClassifier(r'C:\Users\Mamatha\Desktop\Emotion-detection-master\src\haarcascade_frontalface_default.xml') 
cam=cv2.VideoCapture(0)
 
while True:
    ret,image=cam.read()
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    face=detect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face:
            cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow('Camera',gray)
    if cv2.waitKey(1) & 0xFF==ord('a'):
       break
cam.release()
cv2.destroyAllWindows()
