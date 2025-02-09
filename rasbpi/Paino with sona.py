#Paino with sona
#sona sener, piezo buzzer

from gpiozero import DistanceSensor,TonalBuzzer
from time import sleep

#senser, buzzer
piezo = TonalBuzzer(21)

sensor = DistanceSensor(echo = 20, trigger = 16)

#main
try:
    while True:
        DistanceCm = sensor.distance*100
        if (DistanceCm >= 0) and (DistanceCm < 10):
            print("do")
            piezo.play(261.6)
        elif(DistanceCm >= 10) and (DistanceCm < 13):
            print("re")
            piezo.play(293.6)
        elif(DistanceCm >= 13) and (DistanceCm < 16):
            print("mi")
            piezo.play(329.6)
        elif(DistanceCm >= 16) and (DistanceCm < 19):
            print("fa")
            piezo.play(349.2)
        elif(DistanceCm >= 19) and (DistanceCm < 22):
            print("sol")
            piezo.play(391.9)
        elif(DistanceCm >= 22) and (DistanceCm < 25):
            print("la")
            piezo.play(440.0)
        elif(DistanceCm >= 25) and (DistanceCm < 28):
            print("si")
            piezo.play(493.9)
        elif(DistanceCm >= 28) and (DistanceCm < 31):
            print("5oc do")
            piezo.play(523.0)
        else:
            pirnt("no data")
            piezo.stop()

        print("cm",DistanceCm)
        sleep(0.5)

#interrupt
except KeyboardInterrupt:
    pass
