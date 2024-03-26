import sys
sys.path.insert(0, '/home/bourk/Documents/projet_plante')
import pymysql
from data.data import *
from data.config import dbConfig


class DB:

    def __init__(self):
        self.conn = None

    def connect(self):
       self.conn = pymysql.connect(
                host = dbConfig["host"],
                user = dbConfig["user"],
                password = dbConfig["password"],
                db = dbConfig["db"],
                charset = dbConfig["charset"],
                cursorclass=pymysql.cursors.DictCursor)

    def insert(self, query):
        try:
            self.connect()
            with self.conn.cursor() as cursor:
                cursor.execute(query)
            self.conn.commit()
        finally:
            self.close()

    def select(self, query):
        try:
            self.connect()
            with self.conn.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        finally:
            self.close()

    def update(self, query):
        try:
            self.connect()
            with self.conn.cursor() as cursor:
                cursor.execute(query)
            self.conn.commit()
        finally:
            self.close()

    def delete(self, query):
        try:
            self.connect()
            with self.conn.cursor() as cursor:
                cursor.execute(query)
            self.conn.commit()
        finally:
            self.close()

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    db = DB()
    query = "insert into test (data) values ('un nouveau test')"
    print(db.insert(query))