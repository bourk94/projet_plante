#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/bourk/Documents/projet_plante')
from ADC.ADCDevice import *
from data.data import *
from util.utils import interruptible_sleep
import time
import threading

class EarthMoistureSensor:

    def __init__(self, adc_device, stop_event):
        self.adc = adc_device
        self.stop_event = stop_event
        self.values = [0]*100
        self.adc_setup()
        
    def adc_setup(self):
        if self.adc.detectI2C(0x38):
            self.adc = PCF8591()
        elif self.adc.detectI2C(0x4b):
            self.adc = ADS7830()
        else:
            print("No correct I2C address found, \n"
                "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
                "Program Exit. \n")
            exit(-1)

    def check_percent(self):
        wateringData["percent"] = (100 * (218 - max(self.values)) / 109)
        if wateringData["percent"] > 100:
            wateringData["percent"] = 100
        if wateringData["percent"] < 0:
            wateringData["percent"] = 0
        return wateringData["percent"]
    
    def check_moisture(self):
        if wateringData["percent"] > wateringData["wateringPercent"]:
            wateringData["is_moist"] = True
            none_critical_errors["moisture"] = False
        else:
            wateringData["is_moist"] = False
            none_critical_errors["moisture"] = True
        return wateringData["is_moist"]        


    def loop(self):
        while not self.stop_event.is_set():
            for i in range(100):
                self.values[i] = self.adc.analogRead(2)
            self.check_percent()
            self.check_moisture()
            print("Moisture : %.2f %%, is_moist : %s"%(wateringData["percent"], wateringData["is_moist"]))
            interruptible_sleep(wateringData["moistureSensorDelay"], self.stop_event)

    def destroy(self):
        self.adc.close()