import os
os.system("echo 5 > /sys/class/gpio/export")
os.system("echo 6 > /sys/class/gpio/export")
os.system("echo 13 > /sys/class/gpio/export")
os.system("echo 19 > /sys/class/gpio/export")
os.system("echo 21 > /sys/class/gpio/export")
os.system("sudo systemctl start pigpiod")
os.system("sudo python face_recognition.py")
