import cv2
import os
import time
import pickle
import common as c
import numpy as np
import RPi.GPIO as GPIO
from gpiozero import Button

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

led_P1 = 12
led_P2 = 16
led_P3 = 18
motor_T1 = 7
motor_T2 = 11
motor_T3 = 13
motor_T4 = 15
button = Button(21)

GPIO.setup(led_P1, GPIO.OUT)
GPIO.setup(led_P2, GPIO.OUT)
GPIO.setup(led_P3, GPIO.OUT)
GPIO.setup(motor_T1, GPIO.OUT)
GPIO.setup(motor_T2, GPIO.OUT)
GPIO.setup(motor_T3, GPIO.OUT)
GPIO.setup(motor_T4, GPIO.OUT)

GPIO.output(led_P1, GPIO.LOW)
GPIO.output(led_P2, GPIO.LOW)
GPIO.output(led_P3, GPIO.HIGH)

face_cascade=cv2.CascadeClassifier("./haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load("trainner.yml")
id_image=0
color_info=(255,255,255)
color_false=(0,0,255)
color_true=(0,255,0)

with open("labels.pickle", "rb") as f:
    og_labels=pickle.load(f)
    labels={v:k for k, v in og_labels.items()}

cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    tickmark=cv2.getTickCount()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, scaleFactor=1.2,minNeighbors=4, minSize=(c.min_size, c.min_size))
    for x, y, w, h in faces:
        gray2=gray[y:y+h, x:x+w]
        id_, conf=recognizer.predict(gray2)
        if conf<=75:
            color=color_true
            name=labels[id_]
        else:
            color=color_false
            name="inconnu"
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_DUPLEX, 1, color_info, 1, cv2.LINE_AA)
        cv2.rectangle(frame, (x,y), (x+w, y+h), color, 2)
        fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
        cv2.imshow("video", frame)
        
        if name == "T1":
            GPIO.output(motor_T1, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(motor_T1, GPIO.LOW)
            time.sleep(2)
        elif name == "T2":
            GPIO.output(motor_T2, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(motor_T2, GPIO.LOW)
            time.sleep(2)
        elif name == "T3":
            GPIO.output(motor_T3, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(motor_T3, GPIO.LOW)
            time.sleep(2)
        elif name == "T4":
            GPIO.output(motor_T4, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(motor_T4, GPIO.LOW)
            time.sleep(2)
        
    if button.is_pressed:
        cap.release() 
        cv2.destroyAllWindows()
        os.system('sudo python face_recording.py')
        
    key=cv2.waitKey(1)
    if key==ord("x"):
        break     
cap.release() 
cv2.destroyAllWindows()     
    


    
