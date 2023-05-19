import cv2
import mediapipe as mp
from time import time
import numpy as np
from playsound import playsound
 
 
# useful variables initilize :
 
mp_drawing=mp.solutions.drawing_utils
mp_drawing_style=mp.solutions.drawing_styles
mp_facemesh=mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
denormalize_coordinates = mp_drawing._normalized_to_pixel_coordinates
mp_face=mp_facemesh.FaceMesh(max_num_faces=2,   refine_landmarks=True )

# The chosen 12 points:   P1,  P2,  P3,  P4,  P5,  P6
chosen_left_eye_idxs  = [362, 385, 387, 263, 373, 380]
chosen_right_eye_idxs = [33,  160, 158, 133, 153, 144]

all_chosen_idxs = chosen_left_eye_idxs + chosen_right_eye_idxs
 

cap=cv2.VideoCapture(0)


# calculate EAR value related functions :
def distance(pt1, pt2):
      dist=sum([(i-j)**2 for i, j in zip(pt1, pt2)])** 0.5
      return dist

def get_ear(landmarks, refer_indx, frame_w, frame_h):
        try:
            # compute horizontal distance between eyes :
            coords_points=[]
            for i in refer_indx:
                  lm=landmarks[i]
                  coord=denormalize_coordinates(lm.x, lm.y, frame_w, frame_h)
                  coords_points.append(coord)
             # Eye landmark (x, y)-coordinates
            P2_P6 = distance(coords_points[1], coords_points[5])
            P3_P5 = distance(coords_points[2], coords_points[4])
            P1_P4 = distance(coords_points[0], coords_points[3])

            # compute ear ratio becz distance function return distance :
            ear=(P2_P6 + P3_P5) / (2.0 * P1_P4)

        except:
            ear=0.0
            coords_points=None

        return ear, coords_points           

def calc_avg(landmarks, left_eye_idxs, right_eye_idxs, img_w, img_h):
      left_ear, left_coordinates= get_ear(landmarks,left_eye_idxs, img_w, img_h )
      right_ear, right_coordinates=get_ear(landmarks, right_eye_idxs, img_w, img_h)

      avg_EAR=(left_ear + right_ear)/ 2.0

      return avg_EAR, (left_coordinates, right_coordinates)

def start_capture():
    # declare variables :

    status=""
    active=0
    drowsy=0
    color=(0,0,0)
    sleep=0
    

    while True:
        ret, frames=cap.read()
        if not ret:
            break
        
        frames=cv2.cvtColor(cv2.flip(frames, 1), cv2.COLOR_BGR2RGB)

        result=mp_face.process(frames).multi_face_landmarks

        frames=cv2.cvtColor(frames, cv2.COLOR_RGB2BGR)

        cpy_frames=frames.copy()
        imgH, imgW, _ = cpy_frames.shape

        # function return EAR (Eye Aspect Ratio) value
        if result:
            for indx, face_lm in enumerate(result):
                landmarks=face_lm.landmark

                # calculate EAR( Eye aspect ratio) values :
                EAR,_= calc_avg(landmarks, chosen_left_eye_idxs, chosen_right_eye_idxs, imgW, imgH)
                
                # Print the EAR value on the custom_chosen_lmk_image.
                cv2.putText(cpy_frames, f"EAR: {round(EAR, 2)}", (1, 24), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 0, 255), 2 )  
        
                # make points on eyes :
                for indx, landmark in enumerate(landmarks):
                    if indx in all_chosen_idxs:
                        pre_cord=denormalize_coordinates(landmark.x, landmark.y, imgW, imgH)
                        cv2.circle(cpy_frames, pre_cord, 3,(255,255,0), -1)
                        

                #Checking if it is blinked
                if(EAR<0.1):
                    sleep+=1
                    drowsy=0
                    active=0
                    if(sleep>6):
                        # print("sleeep",sleep)
                        playsound('../sound2.mp3')
                        status="SLEEPING!!"
                        color=(0,0,255)
                    
                            
                elif(EAR>0.1 and EAR<=0.2):
                    drowsy+=1
                    active=0
                    sleep=0
                    if(drowsy>6):
                        # print("drowsy",drowsy)
                        status="Drowsy !"
                        color = (0,0,255)
                    
                else:
                    active+=1
                    drowsy=0
                    sleep=0
                    if (active>6):
                        # print("active",active)
                        status="Active"
                        color=(0,255,0)
                

                cv2.putText(cpy_frames, status, (5,125), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color,2)

        # showing result video:
        cv2.imshow("Face Detection", cpy_frames)

        if cv2.waitKey(2)==27:
            break


start_capture()