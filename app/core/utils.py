class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def build_dictionary(key: list, values: list):
    """build dictionary from key and values"""
    return [dict(zip(key, v)) for v in values]


get_all_keys = [
    "providerID",
    "name",
    "active",
    "department",
    "organization",
    "location",
    "address",
]
