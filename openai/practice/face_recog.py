import cv2

face_cap=cv2.CascadeClassifier('../opencvfile/haar-cascade-files/haarcascade_frontalface_default.xml')

eye_cap=cv2.CascadeClassifier('../opencvfile/haar-cascade-files/haarcascade_eye.xml')

cap=cv2.VideoCapture("../video/human.mp4")


while True:
    ret, frames=cap.read()

    color=cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    # detect face :
    faces=face_cap.detectMultiScale(color, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

    for (x,y,w,h) in faces:
        cv2.rectangle(frames, (x,y),(x+w, y+h),(0,255,0),2)
        roi_gray=color[y:y+h, x:x+w]
        roi_color=frames[y:y+h, x:x+w]

        eyes=eye_cap.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),2)

    if ret:
        cv2.imshow("video",frames)
        if cv2.waitKey(2)==27:
            break
         
cap.release()