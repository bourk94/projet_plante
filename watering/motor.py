#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
from data.data import *

class Motor:

    def __init__(self):
        self.motorPins =  pins["motorPins"]
        GPIO.setmode(GPIO.BOARD)
        for pin in self.motorPins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        
        self.CCWStep = (0x01,0x02,0x04,0x08) # define power supply order for rotating anticlockwise
        self.CWStep = (0x08,0x04,0x02,0x01)  # define power supply order for rotating clockwise

    def moveOnePeriod(self, direction,ms):    
        for j in range(0,4,1):      # cycle for power supply order
            for i in range(0,4,1):  # assign to each pin
                if (direction == 1):# power supply order clockwise
                    GPIO.output(self.motorPins[i], GPIO.HIGH if (self.CCWStep[j] == 1<<i) else GPIO.LOW)
                else :              # power supply order anticlockwise
                    GPIO.output(self.motorPins[i], GPIO.HIGH if self.CWStep[j] == 1<<i else GPIO.LOW)
            if(ms<3):       # the delay can not be less than 3ms, otherwise it will exceed speed limit of the motor
                ms = 3
            time.sleep(ms*0.001)    

    def moveSteps(self, direction, ms, steps):
        for i in range(steps):
            self.moveOnePeriod(direction, ms)

    def motorStop(self):
        for pin in self.motorPins:
            GPIO.output(pin, GPIO.LOW)