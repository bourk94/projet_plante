#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/bourk/Documents/projet_plante')
import RPi.GPIO as GPIO
import datetime
import signal
import sys
import threading
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
        self.stop_event.set()

    def lumiere_on(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.output(self.pin, GPIO.LOW)
        

    def lumiere_off(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.HIGH)
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
        if self.stop_event.is_set():
            self.cleanup()

    def cleanup(self):
        GPIO.cleanup()
