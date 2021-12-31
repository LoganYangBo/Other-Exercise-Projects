import cv2
import glob

imgs=glob.glob("*.jpg")
width=input("Enter the width:")
height=input("Enter the height:")

for image in imgs:
    img=cv2.imread(image,0)   
    re=cv2.resize(img,(int(width),int(height)))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized.jpg"+image,re) 
