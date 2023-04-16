
import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np
import os
folderPath = 'frames'
mylist = os.listdir(folderPath)
graphic = [cv2.imread(f'(folderPath)/{imPath}') for imPath in mylist]
intro = graphic[1];
kill = graphic[2];
winner = graphic[3];
cam = cv2.VideoCapture(0)
detector = HandTrackingModule.HandDetector(maxHands=1,detectionCon=0.77)

folderPath = 'img'
mylist1 = os.listdir(folderPath)
graphic1 = [cv2.imread(f'(folderPath)/{imPath}') for imPath in mylist1]
sqr_img = graphic1[4];
mlsa =  graphic1[5];

gameOver = False
NotWon =True

while NotWon:
    cv2.imshow('Cookie Cutter', cv2.resize(intro, (0, 0), fx=0.69, fy=0.69))
    if cv2.waitKey(1) & 0xFF == ord('Q'):
        break

while not gameOver:
        continue

if NotWon:
    for i in range(10):
          cv2.imshow('Cookie Cutter', cv2.resize(kill, (0, 0), fx=0.69, fy=0.69))
    
    while NotWon:
        cv2.imshow('Cookie Cutter', cv2.resize(kill, (0, 0), fx=0.69, fy=0.69))
        if cv2.waitKey(10) & 0xFF == ord('Q'):
            break

else:
      cv2.imshow('Cookie Cutter', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
      cv2.waitKey(125)
   
while NotWon:
        cv2.imshow('Cookie Cutter', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
        if cv2.waitKey(10) & 0xFF == ord('Q'):
            break

cv2.destroyAllWindows()
