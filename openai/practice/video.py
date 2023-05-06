import cv2
import numpy

cap=cv2.VideoCapture("../image/video1.mp4")
 

while cap.isOpened():
    ret, frame=cap.read()
    if ret:
        image=cv2.resize(frame, (600,400))
        cv2.imshow("video", image)
        if cv2.waitKey(23) & 0xff == ord('q'):
            break
    else :
        break    

cv2.destroyAllWindows()        
cap.release()