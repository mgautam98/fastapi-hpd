from app.config import settings
from app.utils import Singleton
import json


class Database(metaclass=Singleton):
    def __init__(self):
        self.db = []

    def add(self, value):
        self.db.append(value)

    def findall(self, id, key='providerID'):
        return [record for record in self.db if record[key] == id]

    def find(self, id, key='providerID'):
        for record in self.db:
            if record[key] == id:
                return record

    def delete(self, id, key='providerID'):
        for idx, record in enumerate(self.db):
            if record[key] == id:
                return self.db.pop(idx)
        return None

    def update(self, id, value, key='providerID'):
        for idx, record in enumerate(self.db):
            if record[key] == id:
                self.db[idx] = value

    def values(self):
        return self.db


db = Database()
