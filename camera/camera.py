#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/bourk/Documents/projet_plante')
import subprocess
import os
import datetime
import time
import threading
from data.data import *

class Camera:

    def __init__(self, stop_event):
        self.stop_event = stop_event
 
    def capture_image(self, output_path):
        command = ["libcamera-jpeg", "-o", output_path]
        try:
            subprocess.run(command, check=True)
            print("Image captured successfully:", output_path)
            none_critical_errors["camera"] = False
        except subprocess.CalledProcessError as e:
            none_critical_errors["camera"] = True
            print("Error while capturing image:", e)

    def loop(self):
        intruders_directory = "/home/bourk/Documents/projet_plante/pictures/intruders/"
        growth_directory = "/home/bourk/Documents/projet_plante/pictures/growth/"
        os.makedirs(intruders_directory, exist_ok=True)
        os.makedirs(growth_directory, exist_ok=True)

        while not self.stop_event.is_set():
            picture_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            current_time = datetime.datetime.now().time()
            if current_time.hour == 12:
                output_path = growth_directory + "image_" + picture_time + ".jpg"
                self.capture_image(output_path)
            if security["intruder"]:
                security["intruder"] = False
                output_path = intruders_directory + "intruder_" + picture_time + ".jpg"
                self.capture_image(output_path)
            time.sleep(0.1)
