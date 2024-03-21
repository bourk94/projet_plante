#!/usr/bin/env python3

import RPi.GPIO as GPIO
import datetime
import signal
import sys
from time import sleep
from data.data import *


class Light:
    def __init__(self, stop_event):
        self.pin = pins["lightPin"]
        self.stop_event = stop_event
        GPIO.setwarnings(False)
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, sig, frame):
        GPIO.cleanup()
        sys.exit(0)

    def lumiere_on(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)
        

    def lumiere_off(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.HIGH)

    def loop(self):
        while not self.stop_event.is_set():
            sleep(0.1)
            current_time = datetime.datetime.now().time()
            if current_time.hour >= 5 and current_time.hour < 17:
                if current_time.hour >= 12  and current_time.minute > 30:
                    self.lumiere_off()
                else:
                    self.lumiere_on()
            else:
                self.lumiere_off()

    def cleanup(self):
        GPIO.cleanup()
