import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import pyfirmata2

board = pyfirmata2.Arduino("COM4")
ledPin = board.get_pin("d:8:o")

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.6, maxHands= 1)

while True:
  _, img = cap.read()
  hands, img = detector.findHands(img)

  if hands:
    hand1 = hands[0]
    fingers = detector.fingersUp(hand1)
    print(fingers)

    if fingers[1] == 1:
      ledPin.write(1)
      sleep(2)
    elif fingers[1] == 1 and fingers[2] == 1:
      ledPin.write(1)
      sleep(2)
      ledPin.write(0)
      sleep(2)
      ledPin.write(1)
      sleep(2)

    elif fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1:
      ledPin.write(1)
      sleep(2)
      ledPin.write(0)
      sleep(2)
      ledPin.write(1)
      sleep(2)
      ledPin.write(0)
      sleep(2)
      ledPin.write(1)
      sleep(2)

    else:
      ledPin.write(0)
      

  cv2.imshow("Window",img)
  if cv2.waitKey(1) == ord("q"):
    break