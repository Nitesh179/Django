import cv2
import numpy as np

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'MJPG')

height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fps=cap.get(cv2.CAP_PROP_FPS)

out=cv2.VideoWriter("../image/vid1.avi", fourcc,fps, (int(width), int(height)))
print("Frames are {}".format(fps))
if(cap.isOpened()):
    while(cap.isOpened()):
        ret, frame=cap.read()
        if ret:
            cv2.imshow('video capture', frame)
            frame=cv2.flip(frame,0)
            out.write(frame)
            if(cv2.waitKey(2)==27) :
                break

out.release()
cap.release()
cv2.destroyAllWindows()
