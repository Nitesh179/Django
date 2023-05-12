import cv2
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_drawing_style=mp.solutions.drawing_styles
mphands=mp.solutions.hands  

cap=cv2.VideoCapture(0)
hands=mphands.Hands() #default 2 hands detect

while True:
    ret, frames=cap.read()
    frames=cv2.cvtColor(cv2.flip(frames, 1), cv2.COLOR_BGR2RGB)
    result=hands.process(frames)
    frames=cv2.cvtColor(frames, cv2.COLOR_RGB2BGR)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frames, hand_landmarks, mphands.HAND_CONNECTIONS)

    cv2.imshow("Hand Detection", frames)
    if cv2.waitKey(2)==27:
        break

cap.release()