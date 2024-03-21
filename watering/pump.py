#!/usr/bin/env python3
import RPi.GPIO as GPIO
import sys
import signal
from data.data import *

class Pump:

    def __init__(self):
        GPIO.setwarnings(False)
        self.pin = pins["pumpPin"]
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        # signal.signal(signal.SIGTERM, self.signal_handler)
        # signal.signal(signal.SIGINT, self.signal_handler)

    def pump_on(self):
        GPIO.output(self.pin, GPIO.LOW)

    def pump_off(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def cleanup(self):
        GPIO.cleanup()

    # def signal_handler(self, sig, frame):
    #     try:    
    #             GPIO.cleanup()
    #     except RuntimeError:
    #         pass

