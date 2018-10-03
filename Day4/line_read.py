import numpy as np
import cv2 

img = np.zeros((512,521,3), np.uint8)

line = cv2.line(img,(0,0),(511,511),(0,255,0),50)
cv2.imshow('draw_line',line)
cv2.waitKey(0)
 
