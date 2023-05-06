import cv2
import numpy,os


listimg=os.listdir('../image')
 
path="/home/dev52/Django/openai/image/"


for i in listimg:
    full_path=path + i
     
    imge=cv2.imread(full_path)
    imge=cv2.resize(imge, (380,280))
    imge1=numpy.hstack((imge, imge))
    imge2=numpy.vstack((imge1, imge1))
    print(imge2)
    cv2.imshow("Image", imge2)
    cv2.waitKey(0)

cv2.destroyAllWindows()    