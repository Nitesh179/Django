import cv2

# image=cv2.imread("img1.jpg", cv2.IMREAD_COLOR)


# cv2.imshow("Image",image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

 
image=cv2.imread("../image/img1.jpg", cv2.IMREAD_COLOR)

image=cv2.resize(image,(780,500))
txt = cv2.putText(image,text="nitesh",org=(100,200),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=3,color=(255,255,255))

cv2.imshow("Image",txt)


cv2.waitKey(0)
cv2.destroyAllWindows()