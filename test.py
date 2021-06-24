import pickle

FILE_NAME = './database'

objects = []
objects.append({'a': 1})
objects.append({'a': 2})
objects.append({'a': 3})
objects.append({'a': 4})
objects.append({'a': 7})
objects.append({'a': 5})
objects.append({'a': 6})

print(objects)

with open(FILE_NAME, 'wb') as f:
    for i in objects:
        pickle.dump(i, f)


with open(FILE_NAME, 'rb') as f:
    x = pickle.load(f)
    print(x)
    x = pickle.load(f)
    print(x)
    x = pickle.load(f)
    print(x)
