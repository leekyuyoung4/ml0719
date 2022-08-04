import pickle

with open('test.txt', 'rb') as f:
    data = pickle.load(f)
    print(type(data))
    print(data)
    