from gpiozero import LED
from time import sleep

#led, GPIO 
led1 = LED(16)
led2 = LED(20)
led3 = LED(21)

#main code
try:
    while 1:
        led1.on()
        led2.on()
        led3.on()
        sleep(1.0) #1sec stay
        led1.off()
        led2.off()
        led3.off()
        sleep(1.0)

#interrupt
except KeyboardInterrupt:
    pass

led1.off()
led2.off()
led3.off()
