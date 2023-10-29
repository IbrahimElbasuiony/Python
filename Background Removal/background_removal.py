import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os



#cap = cv2.VideoCapture(0)

#cap.set(3,680)
#cap.set(4,480)

segmentor = SelfiSegmentation(1)

def remove_replace_background(img_url,imgr_url):
    img = cv2.imread(img_url)

    h,w,c = img.shape

    img_replace = cv2.imread(imgr_url)
    h,w,c = img_replace.shape


    resized_image = cv2.resize(img,(w,h))
    img = segmentor.removeBG(resized_image,imgBg=img_replace,cutThreshold=0.5)

    cv2.imwrite("background_sdasd.jpg",img)
    cv2.imshow("image",img)
    cv2.waitKey(1)

def remove_replace_videoBackground(imgereplace):
    cap = cv2.VideoCapture(0)
    cap.set(3,480)
    cap.set(4,640)
    resized_img = cv2.resize(imgereplace,(640,480))

    while True:
        success, img = cap.read()
        img_output = segmentor.removeBG(img,resized_img,cutThreshold=0.5)
        imgaeStack = cvzone.stackImages([img,img_output],2,1)
        cv2.imshow("Image", imgaeStack)
        cv2.waitKey(1)



def remove_replace_BackgroundFolder(folder_dir):
    list_img = os.listdir(folder_dir)
    img_list = []

    for img_path in list_img:
        print(img_path)
        img = cv2.imread(folder_dir+ "/" + img_path)
        ressized_img = cv2.resize(img,(640,480))
        img_list.append(ressized_img)

    
    print(len(img_list))

    img = img_list[0]
    print(type(img))
    img_index = 0


    cap = cv2.VideoCapture(0)
    cap.set(3,480)
    cap.set(4,640)

    while True:
        success, img = cap.read()
        img_output = segmentor.removeBG(img,img_list[img_index],cutThreshold=0.5)
        imgaeStack = cvzone.stackImages([img,img_output],2,1)
        cv2.imshow("Image", imgaeStack)
        key =cv2.waitKey(1)

        if key ==ord('a'):
            if img_index >= 0:
                img_index -=1
        elif key == ord('d'):
            if img_index < len(img_list):
                img_index += 1
        elif key== ord('q'):
            break






folder_url = r"D:\ckgrounds\New folder"

remove_replace_BackgroundFolder(folder_url)

