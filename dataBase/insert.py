import sys
sys.path.insert(0, '/home/bourk/Documents/projet_plante')
from dataBase.DB import DB
from data.data import *
from util.utils import *


class insertDB:
    
    def __init__(self, stop_event, delay):
        self.stop_event = stop_event
        self.delay = delay

    def insertRoomData(self):
        while not self.stop_event.is_set():
            db = DB()
            try:
                db.insert(f"INSERT INTO room (`temperature`, `humidity`) VALUES ('{round(roomData['temperature'])}', '{roomData['humidity']}')")
                print("Inserting data into DB")
                interruptible_sleep(self.delay, self.stop_event)
            except Exception as e:
                print("An error occurred: ", e)
                pass