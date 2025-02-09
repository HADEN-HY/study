#bluetooth smart LED control
#using bluetooth module(HM-10), green,red,blue LED, 220ohm register

import serial
import RPi.GPIO as GPIO

# GPIO 
GREEN_PIN = 16
BLUE_PIN = 20
RED_PIN = 21

# GPIO set
GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
GPIO.setup(RED_PIN, GPIO.OUT)

# BLE Serial set
bleSerial = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)

# main
try:
    while True:
        data = bleSerial.readline()  
        data = data.decode()
        if data.find("green_on") >= 0:
            GPIO.output(GREEN_PIN, GPIO.HIGH) 
            print("green on")
        elif data.find("green_off") >= 0:
            GPIO.output(GREEN_PIN, GPIO.LOW) 
            print("green off")
        elif data.find("blue_on") >= 0:
            GPIO.output(BLUE_PIN, GPIO.HIGH)  
            print("blue on")
        elif data.find("blue_off") >= 0:
            GPIO.output(BLUE_PIN, GPIO.LOW) 
            print("blue off")
        elif data.find("red_on") >= 0:
            GPIO.output(RED_PIN, GPIO.HIGH) 
            print("red on")
        elif data.find("red_off") >= 0:
            GPIO.output(RED_PIN, GPIO.LOW)  
            print("red off")
        
except KeyboardInterrupt:
    pass

bleSerial.close()
GPIO.cleanup()
