import cv2
import numpy as np
import matplotlib.pyplot as plt

canvas=np.zeros((500,500,3))

cv2.line(canvas, (0,0), (100,100), (0,255,0), 2, cv2.LINE_4)
cv2.line(canvas, (0,20), (120,120), (0,255,0), 2, cv2.LINE_AA)

cv2.rectangle(canvas, (200,200), (250,270), (0,0,255),-1)

cv2.circle(canvas, (250,250), 10, (255,0,0))


# cv2.imshow('shapes', canvas)
plt.imshow(canvas)
plt.show()
cv2.waitKey(5000)