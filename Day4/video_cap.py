import numpy as np
import cv2

cap = cv2.VideoCapture(2)

while(True):
	ret, frame = cap.read()
	cv2.imshow('frame',frame)
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('gray',gray)
	image90 = np.rot90(gray)
	cv2.imshow('gray-90',image90)
	rgb90 = np.rot90(frame)
	cv2.imshow('rgb-90',rgb90)
	if cv2.waitKey(1)& 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

