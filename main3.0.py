from gpiozero import Button
import RPi.GPIO as GPIO
import cv2
import operator
import common as c
import os
import glob
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

led_P1 = 12
led_P2 = 16
led_P3 = 18
button5 = Button(5)
button6 = Button(6)
button13 = Button(13)
button19 = Button(19)

GPIO.setup(led_P1, GPIO.OUT)
GPIO.setup(led_P2, GPIO.OUT)
GPIO.setup(led_P3, GPIO.OUT)
GPIO.output(led_P1, GPIO.HIGH)
GPIO.output(led_P2, GPIO.LOW)
GPIO.output(led_P3, GPIO.LOW)

face_cascade=cv2.CascadeClassifier("./haarcascade_frontalface_alt2.xml")
cap=cv2.VideoCapture(0)
QUIT = False
id = 0

while True:
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(c.min_size, c.min_size))
    key=cv2.waitKey(1)
    if button5.is_pressed:
        nb = 0
        for s in glob.glob("/home/pi/Documents/AI_Face/images/T1/*.png"):
            os.remove(s)
        for x, y, w, h in face:
            while nb < 150:
                cv2.imwrite("/home/pi/Documents/AI_Face/images/T1/patient_T1-{:d}.png".format(id), frame[y:y+h, x:x+w])
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
                id+=1
                nb+=1
                ret, frame=cap.read()
                time.sleep(0.2)
            QUIT = True
    if button6.is_pressed:
        nb = 0
        for s in glob.glob("/home/pi/Documents/AI_Face/images/T2/*.png"):
            os.remove(s)
        for x, y, w, h in face:
            while nb < 150:
                cv2.imwrite("/home/pi/Documents/AI_Face/images/T2/patient_T2-{:d}.png".format(id), frame[y:y+h, x:x+w])
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
                id+=1
                nb+=1
                ret, frame=cap.read()
                time.sleep(0.2)
            QUIT = True
    if button13.is_pressed:
        nb = 0
        for s in glob.glob("/home/pi/Documents/AI_Face/images/T3/*.png"):
            os.remove(s)
        for x, y, w, h in face:
            while nb < 150:
                cv2.imwrite("/home/pi/Documents/AI_Face/images/T3/patient_T3-{:d}.png".format(id), frame[y:y+h, x:x+w])
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
                id+=1
                nb+=1
                ret, frame=cap.read()
                time.sleep(0.2)
            QUIT = True
    if button19.is_pressed:
        nb = 0
        for s in glob.glob("/home/pi/Documents/AI_Face/images/T4/*.png"):
            os.remove(s)
        for x, y, w, h in face:
            while nb < 150:
                cv2.imwrite("/home/pi/Documents/AI_Face/images/T4/patient_T4-{:d}.png".format(id), frame[y:y+h, x:x+w])
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
                id+=1
                nb+=1
                ret, frame=cap.read()
                time.sleep(0.2)
            QUIT = True
    if QUIT == True:
        cv2.destroyAllWindows()
        cap.release()
        os.system('sudo python main4.0.py') 
    cv2.imshow("video", frame)
    for jump in range(4):
        ret, frame=cap.read()
cap.release() 
cv2.destroyAllWindows() 
