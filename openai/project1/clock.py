import cv2
import matplotlib.pyplot as plt
from constants import RADIUS, CENTER, CANVAS_SIZE, COLORS
import numpy as np
from hfunctions import get_ticks, draw_time 

image=np.zeros(CANVAS_SIZE, dtype=np.uint8)
image[:]=[255,255,255]

#get the starting and ending points of ticks in the watch
hours_init, hours_dest = get_ticks()
 

# draw all the ticks for loop :
for i in range(len(hours_init)):
    if i%5 == 0: 
      
      cv2.line(image, hours_init[i], hours_dest[i], COLORS['black'], 3)
     
    else:
        cv2.circle(image, hours_init[i], 5, COLORS['gray'], -1)


#Draw some decorations on the watch
cv2.circle(image, CENTER, RADIUS+10, COLORS['brown'], 5)
cv2.putText(image, "TITAN", (215,230), cv2.FONT_HERSHEY_TRIPLEX, 2, COLORS['dark_gray'], 1, cv2.LINE_AA)

while True:
   orgimg=image.copy()
   clock_face=draw_time(orgimg)

   cv2.imshow('Clock', orgimg)
  #  plt.imshow(orgimg)
  #  plt.show()

   if(cv2.waitKey(2)==27):
      break

cv2.destroyAllWindows()