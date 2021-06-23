from app.config import settings
from app.utils import Singleton
import json


class Database(metaclass=Singleton):
    def __init__(self, path):
        self.path = path
        self.db = {}
        self._load()

    def _load(self):
        with open(self.path, 'r') as f:
            self.db = json.load(f)

    def _save(self):
        with open(self.path, 'w') as f:
            json.dump(self.db, f)

    def __getitem__(self, key):
        return self.db[self._key(key)]

    def __setitem__(self, key, value):
        self.db[self._key(key)] = value
        self._save()

    def get(self, key):
        return self.db.get(self._key(key))

    def __repr__(self):
        return self.db.__repr__()

    def _key(self, key: int):
        return key.__str__()

    def pop(self, key: int, default=None):
        res = self.db.pop(self._key(key), default)
        self._save()
        return res


db = Database(path=settings.DATABASE_PATH)


# # Part 1
# db = {}
