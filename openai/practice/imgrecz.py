import cv2

# image=cv2.imread("img1.jpg", cv2.IMREAD_COLOR)


# cv2.imshow("Image",image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

 
image=cv2.imread("../image/img1.jpg", cv2.IMREAD_COLOR)

image=cv2.resize(image, ())
cv2.imshow("Image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()