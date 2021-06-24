from app.config import settings
from app.utils import Singleton
import json


class Database(metaclass=Singleton):
    def __init__(self, path='./'):
        self.path = path
        self.db = []
        self.path = path

    def __load(self):
        with open(self.path, 'r') as f:
            self.db = json.load(f)

    def __save(self):
        with open(self.path, 'w') as f:
            json.dump(self.db, f, ensure_ascii=False, indent=4)

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


db = Database(path=settings.DATABASE_PATH)
