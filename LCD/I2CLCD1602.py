#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/bourk/Documents/projet_plante/LCD')
sys.path.insert(0, '/home/bourk/Documents/projet_plante')
from time import sleep
import threading
import RPi.GPIO as GPIO
from LCD1602 import CharLCD1602
from data.data import *



class LCD:

    def __init__(self, stop_event):
        self.stop_event = stop_event
        self.lcd1602 = CharLCD1602()

    def loop(self):
        self.lcd1602.init_lcd()
        while not self.stop_event.is_set():
            self.lcd1602.write(0, 0, 'Temp. : ' + str(round(roomData["temperature"], 2)) + ' C')
            self.lcd1602.write(0, 1, 'Humidity: ' + str(round(roomData["humidity"], 2)) + ' %')
            sleep(1)

    def destroy(self):
        self.lcd1602.clear()
        GPIO.cleanup()

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        stop_event = threading.Event()
        lcd = LCD(stop_event)
        lcd.loop()
    except KeyboardInterrupt:
        lcd.destroy()
        print("Ending program")