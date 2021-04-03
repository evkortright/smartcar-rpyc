import rpyc
import time
from Led import *

leds = [0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x01, 0x02]

carStateServer = rpyc.connect("localhost", 18861)

try:
    signalOn = False
    while True:
        state = carStateServer.root.get_state()
        print(state)
        led.ledIndex(leds[2]+leds[1],0,0,0)
        led.ledIndex(leds[5]+leds[6],0,0,0)
        if state["signal"] != "none":
            # print("signal ", state["signal"], signalOn)
            if (state["signal"] == "left"):
                if (signalOn):
                    led.ledIndex(leds[2]+leds[1],225,128,0)
            elif (state["signal"] == "right"):
                if (signalOn):
                    led.ledIndex(leds[5]+leds[6],225,128,0)
            signalOn = not signalOn
        time.sleep(0.25)
except KeyboardInterrupt:
    print ("End of Program")
