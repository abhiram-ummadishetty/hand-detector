import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import numpy as np


cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
timeout = 3

start_time = time.time()






detector = HandDetector(detectionCon=0.8,maxHands=1)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        lmList = hands[0]['lmList']
        x, y, w, h = hands[0]['bbox']
        x1,y1,z1 = lmList[4]
        x2,y2,z2 = lmList[16]
        x3,y3,z3 = lmList[20]
        x4,y4,z4 = lmList[8]
        x5,y5,z5 = lmList[12]
        x6,y6,z6 = lmList[0]
        cx, cy = (x1 + x2+ x3) // 3, (y1 + y2+ x3) // 2


        cv2.circle(img,(x1,y1),15, (255,0,255),cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x3, y3), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.line(img, (x1, y1), (x3, y3), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        distance1 = np.sqrt((x2-x1)**2+(y2-y1)**2)
        distance2 = np.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        distance3 = np.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        distance4 = np.sqrt((x4 - x6) ** 2 + (y4 - y6) ** 2)
        distance5 = np.sqrt((x5 - x6) ** 2 + (y5 - y6) ** 2)
        print(int(distance5),int(distance4))

        desired_condition = distance1<80 and distance3<80 and distance2  < 80 and distance4>350 and distance5>350



            # Break the loop if the condition is met or the timeout is reached
        if desired_condition and time.time() - start_time > timeout:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
            cv2.imwrite("captured_image.jpg", img)
            break

        #
        # if distance1<80 and distance3<80 and distance2 < 80:
        #     cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
        #     time.sleep(1)
        #     cv2.imwrite("captured_image.jpg", img)





    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
