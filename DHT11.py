#!/usr/bin/env python3
import time
import threading
import Freenove_DHT as DHT
from data.data import *

class DHT11Sensor:
    def __init__(self, stop_event):
        self.stop_event = stop_event
        self.DHTPin = pins["dthPin"]
        self.dht = DHT.DHT(self.DHTPin, stop_event)

    def loopDHT11(self):
        while not self.stop_event.is_set():
            chk = self.dht.readDHT11()
            if chk == 0:  # Considérer tout résultat égal à 0 comme un succès
                roomData["humidity"] = self.dht.humidity
                print("Humidity: %.2f %%" % roomData["humidity"])
            time.sleep(2)

# if __name__ == '__main__':
#     stop_event = threading.Event()
#     DHTPin = pins["dthPin"]
#     dht_sensor = DHT11Sensor(DHTPin)

#     print('Program is starting ... ')
#     try:
#         dht_sensor.loopDHT11()
#     except KeyboardInterrupt:
#         pass
#     finally:
#         stop_event.set()
#         exit()