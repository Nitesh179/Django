import cv2
import os

listimg=os.listdir('image')
 
path="/home/dev52/Django/openai/image/"

for i in listimg:
    full_path=path + i
    imge=cv2.imread(full_path)
    imge=cv2.resize(imge, (1280,780))
    cv2.imshow("Image", imge)
    cv2.waitKey(0)

cv2.destroyAllWindows()    