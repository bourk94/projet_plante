from ADC.ADCDevice import *
from data.data import *
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
        return wateringData["percent"]
    
    def check_moisture(self):
        if wateringData["percent"] > 5:
            wateringData["is_moist"] = True
        else:
            wateringData["is_moist"] = False
        return wateringData["is_moist"]        


    def loop(self):
        while not self.stop_event.is_set():
            for i in range(100):
                self.values[i] = self.adc.analogRead(2)
            self.check_percent()
            self.check_moisture()
            print("Moisture : %.2f %%, is_moist : %s"%(wateringData["percent"], wateringData["is_moist"]))
            time.sleep(wateringData["moistureSensorDelay"])

    def destroy(self):
        self.adc.close()

if __name__ == '__main__':
    # Create a stop event
    stop_event = threading.Event()

    # Create an instance of the ADCDevice class before creating an instance of the EarthMoistureSensor class
    adc_device_instance = ADCDevice()
    earthMoistureSensor_instance = EarthMoistureSensor(adc_device_instance, stop_event)

    print('Program is starting ... ')
    try:
        earthMoistureSensor_instance.loop()
    except KeyboardInterrupt:
        print("Exiting")
        pass
    finally:
        stop_event.set()
        earthMoistureSensor_instance.destroy()
        exit()