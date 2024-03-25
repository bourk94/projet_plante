import sys
sys.path.insert(0, '/home/bourk/Documents/projet_plante')
import RPi.GPIO as GPIO
import time
import threading
from data.data import *

class WaterLevelSensor:
    def __init__(self, stop_event):
        self.stop_event = stop_event
        self.pin = pins["waterLevelSensor"]
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


    def loop(self):
        currentState = False
        previousState = False
   
        while not self.stop_event.is_set():
            time.sleep(0.1)
            if GPIO.input(self.pin) == GPIO.LOW:
                currentState = True
            else:
                currentState = False

            if currentState and not previousState:
                print("Water level is high!")
                previousState = True
                wateringData["is_water_level_low"] = True
                critical_errors["waterLevel"] = False
            elif previousState and not currentState:
                print("Water level is low!")
                previousState = False
                wateringData["is_water_level_low"] = False
                critical_errors["waterLevel"] = True
        if self.stop_event.is_set():
            self.cleanup()

    def cleanup(self):
        GPIO.cleanup()