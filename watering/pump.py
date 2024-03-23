#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/bourk/Documents/projet_plante')
import RPi.GPIO as GPIO
import sys
import signal
import time
import threading
from data.data import *

class Pump:

    def __init__(self):
        GPIO.setwarnings(False)
        self.pin = pins["pumpPin"]
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.HIGH)
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, sig, frame):
        self.cleanup()

    def pump_on(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.output(self.pin, GPIO.LOW)

    def pump_off(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.output(self.pin, GPIO.HIGH)

    def cleanup(self):
        self.pump_off()
        GPIO.cleanup()