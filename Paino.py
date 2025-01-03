#paino
#piezo buzzer, button*5

from gpiozero import Button
import time

#sw, buzzer
sw1 = Button(14)
sw2 = Button(15)
sw3 = Button(18)
sw4 = Button(23)
sw5 = Button(24)

piezo = TonalBuzzer(21)

#main
try:
    while 1:
        if sw1.is_pressed:
            print("do")
            piezo.paly(261.6)
        if sw2.is_pressed:
            print("re")
            piezo.paly(293.6)
        if sw3.is_pressed:
            print("mi")
            piezo.paly(329.6)
        if sw4.is_pressed:
            print("fa")
            piezo.paly(349.2)
        if sw5.is_pressed:
            print("sol")
            piezo.paly(391.9)
        else:
            pass
    time.sleep(0.1)

except KeyboardInterrupt:
    pass