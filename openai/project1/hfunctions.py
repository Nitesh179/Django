import cv2
import math
import datetime
from constants import COLORS, CENTER, RADIUS

def get_ticks():
    hours_init=[]
    hours_dest=[]
    
    for i in range(0,360,6):
       x_axis=int(CENTER[1]+RADIUS*math.cos(i*math.pi/180))
       y_axis=int(CENTER[1]+RADIUS*math.sin(i*math.pi/180))

       hours_init.append((x_axis,y_axis))

    for i in range(0,360,6):
       x_axis=int(CENTER[1]+(RADIUS-20)*math.cos(i*math.pi/180))
       y_axis=int(CENTER[1]+(RADIUS-20)*math.sin(i*math.pi/180))

       hours_dest.append((x_axis,y_axis))

    return hours_init, hours_dest   
          

def draw_time(image):
    time_now=datetime.datetime.now().time()
    hour=math.fmod(time_now.hour, 12)  # 24 hours formate convert to 12 hours
    minute=time_now.minute
    second=time_now.second

    second_angle=math.fmod(second * 6 + 270, 360)
    minute_angle=math.fmod(minute * 6 + 270, 360)
    hour_angle=math.fmod((hour * 30) + (minute/2) +270, 360)
   
    int(CENTER[0] + (RADIUS-25) * math.cos(second_angle * math.pi / 180))

draw_time("image")    