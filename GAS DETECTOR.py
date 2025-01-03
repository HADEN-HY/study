#GAS DETECTOR
#MQ-2 gas module, MCP3208, buzzer

from gpiozero import Buzzer, MCP3208
import time

#senser,buzzer 
bz = Buzzer(18)
gas = MCP3208(channel=0)

try:
    while 1:
        gasValue = gas.value * 100
        print(gasValue)
        if gasValue >=10:
            bz.on()
        else:
            bz.off()
        
        time.sleep(0.2)

#interrupt
except KeyboardInterrupt:
    pass
bz.off()