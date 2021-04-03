import rpyc
import time

lightsServer = rpyc.connect("localhost", 18861)

print(lightsServer.root.get_state())

lightsServer.root.signal("left")

print(lightsServer.root.get_state())

time.sleep(5)

lightsServer.root.signal("right")

print(lightsServer.root.get_state())

time.sleep(2)

print(lightsServer.root.get_state())

lightsServer.root.move("fwd")

time.sleep(2)

lightsServer.root.move("stop")

lightsServer.root.signal("none")

time.sleep(2)

lightsServer.root.move("rev")
lightsServer.root.signal("left")

time.sleep(2)

lightsServer.root.move("stop")

lightsServer.root.signal("none")

time.sleep(2)

print("End of test")


