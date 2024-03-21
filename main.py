import threading
import time
from watering.earthMoistureSensor import EarthMoistureSensor
from watering.pump import Pump
from watering.motor import Motor
from ADC.ADCDevice import ADCDevice
from data.data import *
from DHT11 import DHT11Sensor
from thermometer.Thermometer import Thermometer
from light.light import Light
from I2CLCD1602 import LCD
from MQTT.MQTT import Mqtt

stop_event = threading.Event()
adc_device_instance = ADCDevice()
motor = Motor()
pump = Pump()

thread_earthMoistureSensor = threading.Thread(target=EarthMoistureSensor(adc_device_instance, stop_event).loop)
thread_temperatureSensor = threading.Thread(target=Thermometer(adc_device_instance, stop_event).loopThermometer)
thread_humiditySensor = threading.Thread(target=DHT11Sensor(stop_event).loopDHT11)
thread_light = threading.Thread(target=Light(stop_event).loop)
thread_lcd = threading.Thread(target=LCD(stop_event).loop)
thread_mqtt = threading.Thread(target=Mqtt(stop_event).loop)


def main():
    thread_earthMoistureSensor.start()
    thread_temperatureSensor.start()
    thread_humiditySensor.start()
    thread_light.start()
    thread_lcd.start()
    thread_mqtt.start()
    while not stop_event.is_set():
      if not wateringData["is_moist"]:
        for motorPosition in motorPostions:
            motor.moveSteps(*motorPostions[motorPosition])
            time.sleep(1)
            pump.pump_on()
            time.sleep(4)
            pump.pump_off()
            time.sleep(2)
        wateringData["is_moist"] = True
        time.sleep(1)



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting")
        pass
    finally:
        stop_event.set()
        thread_mqtt.join()
        thread_temperatureSensor.join()
        thread_humiditySensor.join()
        thread_light.join()
        thread_lcd.join()
        thread_earthMoistureSensor.join()
        adc_device_instance.close()
        exit()