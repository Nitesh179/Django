import cv2 
import matplotlib.pyplot as plt
import numpy as np, cv2

image=cv2.imread("../image/flower.webp")
 
# plt.imshow(image)

# plt.show()
 
# We have read the image with OpenCV and visualized it with the matplotlib library. The color has been changed because OpenCV reads the image in BGR format instead of RGB, but matplotlib expects the image in RGB format. So, we need to convert the image from BGR to RGB.
#  Converting the image from BGR to RGB format :

'''RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BayerGR2GRAY)

 
plt.imshow(gray, cmap='gray')

plt.show()
 
#  Rotating the image :
colorchange = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
rotate = cv2.rotate(colorchange, cv2.ROTATE_180 ) 

plt.imshow(rotate)
plt.show()'''


# Draw on image Rectangle :

'''convert=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img=cv2.rectangle(convert, pt1=(1000,1700), pt2=(2500,3300), color=(255,0,0),thickness=15)
# print(image.shape)
plt.imshow(img)
plt.show()
'''

 
vis = np.zeros((384, 836), np.float32)
h,w = vis.shape
vis2 = cv2.CreateMat(h, w, cv2.CV_32FC3)
vis0 = cv2.fromarray(vis)
cv2.CvtColor(vis0, vis2, cv2.CV_GRAY2BGR)
