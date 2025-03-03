import os
import random
from settings import input_csv_path
import csv
data = [[random.uniform(-1e38, 1e38) for _ in range(1000000)] for _ in range(10)]
data[0].sort()
data[-1].sort(reverse=True)


with open(input_csv_path, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)