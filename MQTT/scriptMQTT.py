import sys
sys.path.insert(0, '/home/bourk/Documents/projet_plante')
import paho.mqtt.client as mqtt
from data.data import *
from data.config import mqttConfig
from util.utils import *
from dataBase.DB import DB


class Mqtt:
    
    def __init__(self, stop_event):
        self.stop_event = stop_event
        self.broker = mqttConfig["broker"]
        self.localhost = mqttConfig["localhost"]
        self.port = mqttConfig["port"]
        self.client = None

    def connection(self):
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        print("Connecting to broker...", self.broker)
        self.client.connect(self.broker, self.port)
        self.client.loop_start()

    def publish(self, topic, message, qos):
        try:
            self.connection()
            self.client.publish(topic, message, qos)
        finally:
            self.close()

    def update_message(self,topic):
        message = roomData.get(topic)
        return message

    def close(self):
        self.client.loop_stop()
        self.client.disconnect()

    def loop(self, topic, delay):
        while not self.stop_event.is_set():
            self.publish(topic, self.update_message(topic), 0)
            print ("publishing on topic: ", topic, "message: ", self.update_message(topic))
            interruptible_sleep(delay, self.stop_event)