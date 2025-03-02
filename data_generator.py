import random
import csv
import pickle

data = [[random.randint(-2**31, 2**31-1) for _ in range(1000000)] for _ in range(10)]
data[0].sort()
data[-1].sort(reverse=True)

with open("data.pickle", "wb") as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)