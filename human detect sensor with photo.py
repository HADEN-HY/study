#human detect sensor with photo

from picamera2 import Picamera2
import time
from gpiozero import MotionSensor
import datetime

#set Sensor pin
pirPin = MotionSensor(16)

#set picam
picam = Picamera2()
camera_config = picam.create_preview_configuration()
picam.configure(camera_config)
picam.start()

#main   
try:
    while True:
        if pirPin.motion_detected:  # MotionSensor
            now = datetime.datetime.now()
            print(now)
            fileName = now.strftime('%Y-%m-%d_%H-%M-%S')  
            picam.capture_file(fileName + '.jpg')  
            time.sleep(0.5) 
        
      
except KeyboardInterrupt:
    pass