#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/bourk/Documents/projet_plante')
import RPi.GPIO as GPIO
import time
import threading
from data.data import *
from util.utils import interruptible_sleep


class MotionSensor:

    def __init__(self, stop_event):
        self.stop_event = stop_event
        GPIO.setmode(GPIO.BOARD)
        self.sensorPin = pins["motionSensor"]
        self.ledPin = pins["motionSensorLed"]
        GPIO.setup(self.sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.ledPin, GPIO.OUT)

    def loop(self):
        currentState = False
        previousState = False
   
        while not self.stop_event.is_set():
            time.sleep(0.1)
            if GPIO.input(self.sensorPin) == GPIO.HIGH:
                currentState = True
            else:
                currentState = False

            if currentState and not previousState:
                print("Intruder detected!")
                previousState = True
                security["intruder"] = True
                GPIO.output(self.ledPin, GPIO.HIGH)
                time.sleep(1.5)
            elif previousState and not currentState:
                print("Intruder left!")
                previousState = False
                security["intruder"] = False
                GPIO.output(self.ledPin, GPIO.LOW)
                interruptible_sleep(60, self.stop_event)
        if self.stop_event.is_set():
            self.cleanup()

    def cleanup(self):
        GPIO.cleanup()