import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller

# create video capture the parameter 0 is used for webcam 

cap = cv2.VideoCapture(0)

# set the capture hight and width
# the parameter 3 is width and 4 is hight

cap.set(3,1280)
cap.set(4,720)

keys = [['Q','W','E','R','T','Y','U','I','O','P'],
        ['A','S','D','F','G','H','J','K','L',';'],
        ['Z','X','C','V','B','N','M',',','.','/']
        ]


keyboard = Controller()

# create hand tracking object

detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.8, minTrackCon=0.5)

def draw_all(img , button_list):
    for button in button_list:
        x,y = button.pos
        w,h = button.size
        cv2.rectangle(img,button.pos,(x+h,y+w),(255,0,255), cv2.FILLED)
        cv2.putText(img, button.text, (x+20, y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
    return img
# create class for the button

class button():
    def __init__(self,text, pos, size = [85,85]):

        self.pos = pos 
        self.text = text 
        self.size = size
    
        
"""
    def draw(self,img):
        x,y = self.pos
        w,h = self.size
        cv2.rectangle(img,self.pos,(x+h,y+w),(255,0,255), cv2.FILLED)
        cv2.putText(img, self.text, (x+25, y+75),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5)
        return img
    
"""


button_list = []
for i in range(len(keys)):
        for x, key in enumerate(keys[i]):
            button_list.append(button(key,pos=[100 * x + 10 ,100 * i +50]))


# set the webcam to run 

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    # send the image to the detector to detect the hand & landmarkes
    hands, img = detector.findHands(img)
    img = draw_all(img,button_list)


    if hands:
          hand1 = hands[0]  # Get the first hand detected
          lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
          bbox1 = hand1["bbox"]  #
            
          for button in button_list:
              x,y = button.pos
              w,h = button.size 


              if x < lmList1[8][0] < x+w and y < lmList1[8][1]< y+h:
                   cv2.rectangle(img,button.pos,(x+h,y+w),(175,0,175), cv2.FILLED)
                   cv2.putText(img, button.text, (x+20, y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)

                   l,_,_ = detector.findDistance(lmList1[8][0:2],lmList1[6][0:2],img)

                   if l < 50:
                        keyboard.press(button.text)
                        cv2.rectangle(img,button.pos,(x+h,y+w),(0,255,0), cv2.FILLED)
                        cv2.putText(img, button.text, (x+20, y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
                        print(f"You clicked on {button.text}")
                        sleep(0.30)



    cv2.imshow("image", img)

    cv2.waitKey(1)

    # the following lines of code is a way to create a keyboard using class and method draw
"""
    q_button = button("Q",pos=[100,100])
    img = q_button.draw(img)
    w_button = button("W",pos=[210,100])
    img = w_button.draw(img)
    e_button = button("E",pos=[320,100])
    img = e_button.draw(img)
    r_button = button("R",pos=[430,100])
    img = r_button.draw(img)

"""


