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
   
    second_x=int(CENTER[0] + (RADIUS-25) * math.cos(second_angle * math.pi / 180))
    second_y=int(CENTER[0] + (RADIUS-25) * math.sin(second_angle * math.pi / 180))
    cv2.line(image, CENTER, (second_x, second_y), COLORS['black'], 2)

    minute_x=int(CENTER[0] + (RADIUS-60) * math.cos(minute_angle * math.pi / 180))
    minute_y=int(CENTER[0] + (RADIUS-60) * math.sin(minute_angle * math.pi / 180))
    cv2.line(image, CENTER, (minute_x, minute_y), COLORS['brown'], 3)

    hour_x=int(CENTER[0] + (RADIUS-100) * math.cos(hour_angle * math.pi / 180))
    hour_y=int(CENTER[0] + (RADIUS-100) * math.sin(hour_angle * math.pi / 180))
    cv2.line(image, CENTER, (hour_x, hour_y), COLORS['amber'], 7)

    cv2.circle(image, CENTER, 5, COLORS['gray'], -1)
    
    day, date=get_time()
    
    cv2.putText(image, date, (200,390), 1, 2, COLORS['gray'], 2, cv2.LINE_AA)
    cv2.putText(image, day, (230,430), 1, 2, COLORS['gray'], 2, cv2.LINE_AA)
   

def get_time():
    dt=datetime.datetime.now()
    day=dt.strftime('%A')
    date=dt.strftime('%b %d, %Y')
    return day, date
