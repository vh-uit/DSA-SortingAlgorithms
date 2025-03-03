import csv
from settings import runtime_configs, input_csv_path, output_csv_path

with open(input_csv_path) as f, open(output_csv_path, mode='w', newline='') as out_file:
    reader = csv.reader(f)
    writer = csv.writer(out_file)
    
    # Write the header row
    writer.writerow(['Data set #', 'Algorithm', 'Runtime'])
    
    for data_index, row in enumerate(reader):
        data = list(map(int, row))
        for name, runtime in runtime_configs:
            result = runtime.measure_runtime(data, 10)
            writer.writerow([data_index, name, result])
            print(f"Data set #{data_index} - {name}: {result}")
