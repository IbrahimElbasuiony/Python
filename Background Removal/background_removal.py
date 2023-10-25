import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation



#cap = cv2.VideoCapture(0)

#cap.set(3,680)
#cap.set(4,480)

segmentor = SelfiSegmentation(1)


img = cv2.imread(r"E:\me\IMG-20230616-WA0003.jpg")

h,w,c = img.shape

img_replace = cv2.imread(r"C:\Users\ibrah\Downloads\paris-night-latin-quarter.jpg")
h,w,c = img_replace.shape


resized_image = cv2.resize(img,(w,h))
img = segmentor.removeBG(resized_image,imgBg=img_replace,cutThreshold=0.5)

cv2.imwrite("background_sdasd.jpg",img)
cv2.imshow("image",img)
cv2.waitKey(1)
"""
while True:
    success, img = cap.read()

    img = cv2.flip(img,2)
    imgout = segmentor.removeBG(img,imgBg=(255,0,255))

    imgstack = cvzone.stackImages([img,imgout],2,1)
    cv2.imshow("image",imgstack)


    cv2.waitKey(1)"""