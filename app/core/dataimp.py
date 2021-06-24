from app.core.utils import Singleton
import pickle
import shelve
import os


class DatabaseShelve(metaclass=Singleton):
    def __init__(self, path='./database/'):
        self.path = path + 'records.pickle'

    def add(self, value, key='providerID'):
        with shelve.open(self.path, 'c') as db:
            db[str(value[key])] = value

    def findall(self, id, key='providerID'):
        with shelve.open(self.path, 'c') as db:
            return [record for record in db.values() if record[key] == id.__str__()]

    def find(self, id):
        with shelve.open(self.path, 'c') as db:
            return db.get(id.__str__())

    def delete(self, id, key='providerID'):
        with shelve.open(self.path, 'c') as db:
            if db.get(id.__str__()):
                del db[id.__str__()]

    def update(self, id, value, key='providerID'):
        with shelve.open(self.path, 'c') as db:
            if db.get(id.__str__()):
                db[id] = value

    def values(self):
        with shelve.open(self.path, 'c') as db:
            return list(db.values())


class FileDatabase(metaclass=Singleton):
    def __init__(self, path='./database/'):
        self.path = path
        self.records_path = os.path.join(self.path, 'records.pickle')
        self.db = []
        self.__load()

    def add(self, value):
        self.db.append(value)
        self.__save(self.db[-1])

    def findall(self, id, key='providerID'):
        return [record for record in self.db if record[key] == id]

    def find(self, id, key='providerID'):
        for record in self.db:
            if record[key] == id:
                return record

    def delete(self, id, key='providerID'):
        for idx, record in enumerate(self.db):
            if record[key] == id:
                res = self.db.pop(idx)
                self.__save_all()
                return res
        return None

    def update(self, id, value, key='providerID'):
        for idx, record in enumerate(self.db):
            if record[key] == id:
                self.db[idx] = value
                self.__save_all()

    def values(self):
        return self.db

    def __save(self, obj):
        with open(self.records_path, 'ab') as f:
            pickle.dump(obj, f)

    def __load(self):
        if not os.path.exists(self.records_path):
            open(self.records_path, 'w').close()

        with open(self.records_path, 'rb+') as f:
            while True:
                try:
                    self.db.append(pickle.load(f))
                except EOFError:
                    break

    def __save_all(self):
        with open(self.records_path, 'wb') as f:
            for record in self.db:
                pickle.dump(record, f)
