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

