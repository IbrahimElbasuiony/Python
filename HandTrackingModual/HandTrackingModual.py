import cv2
import mediapipe as mp


class HandTrackingModul:
    def __init__(self, mode = False, maxHands = 2, Detectcon = 0.5, Trackingcon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.Detectioncon = Detectcon
        self.Trackingcon = Trackingcon


        self.Mhands = mp.solutions.hands

        self.mpDraw = mp.solutions.drawing_utils
        self.hands = self.Mhands.Hands()

    def FindHands(self,img, draw=True):

        RBGImage = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        self.result = self.hands.process(RBGImage)



        if self.result.multi_hand_landmarks:
            for handLM in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLM,self.Mhands.HAND_CONNECTIONS)
        return img


    def findPosition(self,img,handNo =0, draw = True):
        landmarks = []
        if self.result.multi_hand_landmarks:

            my_hand = self.result.multi_hand_landmarks[handNo]
            for id, lm in enumerate(my_hand.landmark):
                h,w,c = img.shape

                cx,cy = int(lm.x * w) , int(lm.y * h)
                landmarks.append([id,cx,cy])

                if draw:
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
        return landmarks
    




def main():
    cap = cv2.VideoCapture(0)

    detector= HandTrackingModul()
    while True:
        sucess, img = cap.read()
        img = detector.FindHands(img)
        lms = detector.findPosition(img)

        if len(lms) != 0:
            print(lms[4])



        cv2.imshow("image",img)

        cv2.waitKey(1)


if __name__ == "__main__":
    main()
