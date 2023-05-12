import cv2

car_cap=cv2.CascadeClassifier('../opencvfile/car/cars.xml')

cap=cv2.VideoCapture('../video/cars2.mp4')


while True:
    ret, frames=cap.read()
    
    color=cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    # cars detect:

    cars=car_cap.detectMultiScale(color, scaleFactor=1.1, minNeighbors=5)

    for(x,y,w,h) in cars:
        cv2.rectangle(frames, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.putText(frames,"car", org=(x,y), fontScale=1, color=(0,0,255), thickness = 1, fontFace=cv2.LINE_AA)

    if ret:
        cv2.imshow('cars video', frames) 

        if cv2.waitKey(2)==27:
            break   

cap.release()
cv2.destroyAllWindows()
