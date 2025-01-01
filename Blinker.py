#blinker

from gpiozero import LED
from time import sleep

#GPIO PIN
carLedRed =2
carLedYellow =3
carLedGreen = 4
humanLedRed = 20
humanLedGreen = 21

#main
try:
    while 1:
        carLedRed.value = 0
        carLedYellow.value = 0
        carLedGreen.value = 1
        humanLedRed.value = 1
        humanLedGreen.value = 0
        sleep(3.0)
        carLedRed.value = 0 
        carLedYellow.value = 1
        carLedGreen.value = 0
        humanLedRed.value = 0
        humanLedGreen.value = 0
        sleep(1.0)
        carLedRed.value = 1
        carLedYellow.value = 0
        carLedGreen.value = 0
        humanLedRed.value = 0
        humanLedGreen.value = 1
        sleep(3.0)

#interrupt
except KeyboardInterrupt:
    pass


carLedRed.value = 0
carLedYellow.value = 0
carLedGreen.value = 0
humanLedRed.value = 0
humanLedGreen.value = 0