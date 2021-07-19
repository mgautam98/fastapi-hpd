class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def build_providers(values: list):
    """build dictionary from key and values"""
    return [dict(zip(get_all_keys, v)) for v in values]


def build_provider(
    provider: list, phone_number: list, qualifications: list, specialities: list
):
    """build dictionary from key and values"""
    provider_dict = dict(zip(get_all_keys, provider[0]))

    provider_dict["phone"] = [x[0] for x in phone_number]
    provider_dict["qualification"] = [x[0] for x in qualifications]
    provider_dict["speciality"] = [x[0] for x in specialities]

    return provider_dict


get_all_keys = [
    "providerID",
    "name",
    "active",
    "department",
    "organization",
    "location",
    "address",
]
