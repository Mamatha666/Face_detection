import cv2
 
cam=cv2.VideoCapture(0)
 
while True:
	ret,image=cam.read()
	cv2.imshow('Camera',image)
	if cv2.waitKey(1) & 0xFF==ord('a'):
	   break
cam.release()
cv2.destroyAllWindows()
