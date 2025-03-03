import random
from settings import input_csv_path, data_folder
import csv
import shutil
import os
import gzip

data = [[random.uniform(-1e38, 1e38) for _ in range(1000000)] for _ in range(10)]
data[0].sort()
data[1].sort(reverse=True)

shutil.rmtree(data_folder, ignore_errors=True)
os.makedirs(data_folder, exist_ok=True)
with gzip.open(input_csv_path + '.gz', 'wt', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)