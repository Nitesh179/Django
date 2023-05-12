import cv2

face_cap=cv2.CascadeClassifier('../opencvfile/haar-cascade-files/haarcascade_frontalface_default.xml')
eye_cap=cv2.CascadeClassifier('../opencvfile/haar-cascade-files/haarcascade_eye.xml')
car_cap=cv2.CascadeClassifier('../opencvfile/car/cars.xml')

cap=cv2.VideoCapture('../video/video.mp4')

while True:
    ret, frames=cap.read()
    frames=cv2.resize(frames, (800,600))
    gray=cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    # detections work :
    face=face_cap.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    car=car_cap.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for(x,y,w,h) in face:
        cv2.rectangle(frames, (x,y), (x+w, y+h), (0,0,255), 2)
        cv2.putText(frames,"face", org=(x,y), fontScale=1, color=(0,0,255), thickness = 1, fontFace=cv2.LINE_AA)

        roi_gray=gray[y:y+h, x:x+w]
        roi_color=frames[y:y+h, x:x+w]

        eyes=eye_cap.detectMultiScale(roi_gray)

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,0,255), 2)

    for(x,y,w,h) in car:

        cv2.rectangle(frames, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frames,"car", org=(x,y), fontScale=1, color=(0,255,0), thickness = 1, fontFace=cv2.LINE_AA)


    if ret:
        cv2.imshow("video detection", frames)
        if cv2.waitKey(2)==27:
            break

cap.release()        
