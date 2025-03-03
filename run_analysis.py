import csv
import gzip
from datetime import datetime
from settings import input_csv_path, output_csv_path, sorting_algorithm_names, shared_library_files, repeat_time
from runtime_measurements import CppSortRuntime, NumpySortRuntime

# Generate a timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# Modify the output file path to include the timestamp
output_csv_path_with_timestamp = output_csv_path.replace('.csv', f'_{timestamp}.csv')

runtime_configs = list(zip(sorting_algorithm_names, [CppSortRuntime(f"libs/{shared_lib_filename}") for shared_lib_filename in shared_library_files] + [NumpySortRuntime()]))

with gzip.open(input_csv_path + '.gz', 'rt', newline='') as f, open(output_csv_path_with_timestamp, mode='w', newline='') as out_file:
    reader = csv.reader(f)
    writer = csv.writer(out_file)
    
    # Write the header row
    writer.writerow(['Data set #', 'Algorithm', 'Runtime'])
    
    for data_index, row in enumerate(reader):
        data = list(map(float, row))
        for name, runtime in runtime_configs:
            result = runtime.measure_runtime(data, repeat_time)
            writer.writerow([data_index, name, result])
            print(f"Data set #{data_index} - {name}: {result}")
