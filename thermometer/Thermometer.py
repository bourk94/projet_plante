import time
import math
import threading
from ADC.ADCDevice import *
from data.data import *

class Thermometer:
    def __init__(self, adc_device, stop_event):
        self.adc = adc_device
        self.stop_event = stop_event
        self.setupThermometer()

    def setupThermometer(self):
        if self.adc.detectI2C(0x48):
            self.adc = PCF8591()
        elif self.adc.detectI2C(0x4b):
            self.adc = ADS7830()
        else:
            print("No correct I2C address found, \n"
                  "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
                  "Program Exit. \n")
            exit(-1)

    def loopThermometer(self):
        while not self.stop_event.is_set():
            value = self.adc.analogRead(0)
            voltage = value / 255.0 * 3.3
            Rt = 10 * voltage / (3.3 - voltage)
            tempK = 1/(1/(273.15 + 25) + math.log(Rt/10)/3950.0)
            roomData["temperature"] = tempK - 273.15
            print("Temperature : %.2f °C"%(roomData["temperature"]))
            time.sleep(1)

    def destroy(self):
        self.adc.close()

if __name__ == '__main__':
    # Create a stop event
    stop_event = threading.Event()

    # Create an instance of the ADCDevice class before creating an instance of the Thermometer class
    adc_device_instance = ADCDevice()
    thermometer_instance = Thermometer(adc_device_instance, stop_event)

    print('Program is starting ... ')
    try:
        thermometer_instance.loopThermometer()
    except KeyboardInterrupt:
        print("Exiting")
        pass
    finally:
        stop_event.set()
        thermometer_instance.destroy()
        exit()