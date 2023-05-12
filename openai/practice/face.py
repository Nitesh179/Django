import cv2
import time
import mediapipe as mp


cap=cv2.VideoCapture('../video/faces.mp4')

mp_drawing=mp.solutions.drawing_utils
mpfaceMesh=mp.solutions.face_mesh
faceMesh=mpfaceMesh.FaceMesh( max_num_faces=5)
draw_spec=mp_drawing.DrawingSpec(thickness=1, circle_radius=1)


while True:
    ret, frames=cap.read()
    frames=cv2.resize(frames, (1000,600))
    rgb=cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
    result=faceMesh.process(rgb)

    if result.multi_face_landmarks:
        for faces in result.multi_face_landmarks:
            mp_drawing.draw_landmarks(frames, faces, mpfaceMesh.FACEMESH_TESSELATION, draw_spec, draw_spec)

    cv2.imshow("face detection", frames)

    if cv2.waitKey(2)==27:
        break

cap.release()    
