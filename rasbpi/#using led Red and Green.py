#using led Red and Green

from gpiozero import LED
import time
import os

Red_Light = LED(2)
Green_Light = LED(3)

def speak(option, msg):
    os.system("espeak {} '{}'".format(option, msg))
#main
try:
    while True: 

        option = '-s 180 -p 50 -a 200 -v ko+f5'


        msg = 'Green Light!'
        speak(option, msg)
        Red_Light.off()
        Green_Light.on()
        time.sleep(5.0)

        msg = 'Red Light!'
        speak(option, msg)
        

        Red_Light.on()
        Green_Light.off()
        time.sleep(5.0)

        

except KeyboardInterrupt:
    pass




        
