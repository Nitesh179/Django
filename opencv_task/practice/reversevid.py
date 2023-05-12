import cv2

cap=cv2.VideoCapture('../image/flower.mp4')
frames=cap.get(cv2.CAP_PROP_FRAME_COUNT)

fps=cap.get(cv2.CAP_PROP_FPS)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)

fourcc=cv2.VideoWriter_fourcc(*'MJPG')
out=cv2.VideoWriter('../image/reverse.mp4', fourcc, fps, (int(width*0.5), int(height*0.5)))

frame_indx=frames-1

if(cap.isOpened()):
    while(frame_indx!=0):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_indx)
        ret, frame=cap.read()
        frame=cv2.resize(frame, (int(width*0.5), int(height*0.5)))

        out.write(frame)
        frame_indx=frame_indx-1
         
        if(frame_indx%100==0):
            print("==> ",frame_indx)

out.release()
cap.release()
cv2.destroyAllWindows()
