#using 220, 10k register, CDS, MCP3208 
from gpiozero import LED,MCP3208
import time

led_white = LED(18)
cds = MCP3208(channel=0)

#main
try:
    while 1:
        cds_value = cds.value*100
        print(cds_value)

        if cds_value < 50:
            led_white.on()
        else:
            led_white.off()
        
        time.sleep(0.2)

except KeyboardInterrupt:
    pass

led_white.off
