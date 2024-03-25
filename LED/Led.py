import sys
sys.path.insert(0, '/home/bourk/Documents/projet_plante')
import RPi.GPIO as GPIO
import time
import threading
from data.data import *

class Led:

    def __init__(self, stop_event):
        self.stop_event = stop_event
        GPIO.setmode(GPIO.BOARD)
        self.red_pin = pins["rgbLedPins"]["red"]
        self.green_pin = pins["rgbLedPins"]["green"]
        self.blue_pin = pins["rgbLedPins"]["blue"]
        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)
        self.red = GPIO.PWM(self.red_pin, 100)
        self.green = GPIO.PWM(self.green_pin, 100)
        self.blue = GPIO.PWM(self.blue_pin, 100)
        self.red.start(0)
        self.green.start(0)
        self.blue.start(0)

    def setColor(self, r_val, g_val, b_val):      # change duty cycle for three pins to r_val,g_val,b_val
        self.red.ChangeDutyCycle(100 - r_val)     # change pwmRed duty cycle to inverted r_val
        self.green.ChangeDutyCycle(100 - g_val)   # change pwmGreen duty cycle to inverted g_val
        self.blue.ChangeDutyCycle(100 - b_val)    # change pwmBlue duty cycle to inverted b_val

    def convert_to_base_100(self, value):
        return (value / 255) * 100
    
    def green_led(self):
        self.setColor(self.convert_to_base_100(ledColor["green"]["r"]), self.convert_to_base_100(ledColor["green"]["g"]), self.convert_to_base_100(ledColor["green"]["b"]))
    
    def yellow_led(self):
        self.setColor(self.convert_to_base_100(ledColor["yellow"]["r"]), self.convert_to_base_100(ledColor["yellow"]["g"]), self.convert_to_base_100(ledColor["yellow"]["b"]))

    def red_led(self):
        self.setColor(self.convert_to_base_100(ledColor["red"]["r"]), self.convert_to_base_100(ledColor["red"]["g"]), self.convert_to_base_100(ledColor["red"]["b"]))

    def loop(self):
        while not self.stop_event.is_set() :
            time.sleep(0.1)
            if any(critical_errors.values()):
                self.red_led()
            elif any(none_critical_errors.values()):
                self.yellow_led()
            else:
                self.green_led()
        if self.stop_event.is_set():
            self.destroy()

    def destroy(self):
        self.red.stop()
        self.green.stop()
        self.blue.stop()
        GPIO.cleanup()