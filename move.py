import rpyc
from Motor import *
import time
from Led import *

motor = Motor()

carStateServer = rpyc.connect("localhost", 18861)

try:
    signalOn = False
    while True:
        moveState = carStateServer.root.get_state()
        # print(moveState)
        if (moveState["move"] == "stop"):
            motor.setMotorModel(0,0,0,0)
        elif (moveState["move"] == "fwd"):
            motor.setMotorModel(750,750,750,750)
        elif (moveState["move"] == "rev"):
            motor.setMotorModel(-750,-750,-750,-750)
        time.sleep(.5)
except KeyboardInterrupt:
    print ("End of Program")
