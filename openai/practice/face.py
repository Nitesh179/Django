import cv2
import mediapipe as mp
from time import time
import numpy as np
import itertools 

mp_drawing=mp.solutions.drawing_utils
mp_drawing_style=mp.solutions.drawing_styles
mp_facemesh=mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
denormalize_coordinates = mp_drawing._normalized_to_pixel_coordinates
mp_face=mp_facemesh.FaceMesh(max_num_faces=2,   refine_landmarks=True )

cap=cv2.VideoCapture(0)

# eyes index :
left_eye_indx=list(mp_facemesh.FACEMESH_LEFT_EYE)
left_eye_indx=set(np.ravel(left_eye_indx))

right_eye_indx=list(mp_facemesh.FACEMESH_RIGHT_EYE)
right_eye_indx=set(np.ravel(right_eye_indx))

all_indx=left_eye_indx.union(right_eye_indx)

# The chosen 12 points:   P1,  P2,  P3,  P4,  P5,  P6
chosen_left_eye_idxs  = [362, 385, 387, 263, 373, 380]
chosen_right_eye_idxs = [33,  160, 158, 133, 153, 144]

all_chosen_idxs = chosen_left_eye_idxs + chosen_right_eye_idxs
 

while True:
    ret, frames=cap.read()
    frames=cv2.cvtColor(cv2.flip(frames, 1), cv2.COLOR_BGR2RGB)

    face_result=mp_face.process(frames)

    frames=cv2.cvtColor(frames, cv2.COLOR_RGB2BGR)
    imgH, imgW, _ = frames.shape

    cpy_frames=frames.copy()

    if face_result.multi_face_landmarks:
        for faceid, face_lm in enumerate(face_result.multi_face_landmarks):
            # mp_drawing.draw_landmarks(cpy_frames, face_lm, mp_facemesh.FACEMESH_TESSELATION, landmark_drawing_spec= drawing_spec,  connection_drawing_spec=drawing_spec)
           
            # Get the object which holds the x, y, and z coordinates for each landmark
            landmarks = face_lm.landmark
            # Iterate over all landmarks.
            # If the landmark_idx is present in either all_idxs or all_chosen_idxs,
            # get the denormalized coordinates and plot circles at those coordinates.

            for indx, landmark in enumerate(landmarks):
                 if indx in all_chosen_idxs:
                      pre_cord=denormalize_coordinates(landmark.x, landmark.y, imgW, imgH)
                      cv2.circle(cpy_frames, pre_cord, 3,(255,255,0), -1)
                      
 
             
    cv2.imshow("Face Detection", cpy_frames)
    if cv2.waitKey(2)==27:
            break