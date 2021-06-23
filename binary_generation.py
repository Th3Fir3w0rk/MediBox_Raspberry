import cv2
import pickle
import os
import common as c
import numpy as np
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

led_P1 = 12
led_P2 = 16
led_P3 = 18

GPIO.setup(led_P1, GPIO.OUT)
GPIO.setup(led_P2, GPIO.OUT)
GPIO.setup(led_P3, GPIO.OUT)
GPIO.output(led_P1, GPIO.LOW)
GPIO.output(led_P2, GPIO.HIGH)
GPIO.output(led_P3, GPIO.LOW)

image_dir="./images/"
current_id=0
label_ids={}
x_train=[]
y_labels=[]

for root, dirs, files in os.walk(image_dir):
    if len(files):
        label=root.split("/")[-1]
        for file in files:
            if file.endswith("png"):
                path=os.path.join(root, file)
                if not label in label_ids:
                    label_ids[label]=current_id
                    current_id+=1
                id_=label_ids[label]
                image=cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                x_train.append(image)
                y_labels.append(id_)
                
with open("labels.pickle", "wb") as f:
    pickle.dump(label_ids, f)
    
x_train=np.array(x_train)
y_labels=np.array(y_labels)
recognizer= cv2.face.createLBPHFaceRecognizer()
recognizer.train(x_train, y_labels)
recognizer.save("trainner.yml")
os.system("sudo python main5.0.py")
        

        
        
    


    


