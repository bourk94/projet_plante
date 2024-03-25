import sys
sys.path.insert(0, '/home/bourk/Documents/projet_plante')
import requests
import time
from data.data import *

class Internet:
    
    def __init__(self, stop_event):
        self.stop_event = stop_event
    
    def check_internet(self):
        url = 'http://www.google.com/'
        timeout = 5
        try:
            _ = requests.get(url, timeout=timeout)
            return True
        except requests.ConnectionError:
            return False
        
    def loop(self):
        while not self.stop_event.is_set():
            time.sleep(1)
            if not self.check_internet():
                critical_errors["internet"] = True
            else:
                critical_errors["internet"] = False



