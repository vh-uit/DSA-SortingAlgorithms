import os
from runtime_measurements import CppSortRuntime, NumpySortRuntime

# Sorting algorithm names for CSV report header
sorting_algorithm_names = os.getenv("SORTING_ALGORITHM_NAMES", "Quick Sort,Heap Sort,Merge Sort,std::sort,Numpy Sort").split(",")

# C++ sorting algorithm filenames
cpp_folder = os.getenv("CPP_FOLDER", "sorting_algorithms")
cpp_files = os.getenv("CPP_FILENAMES", "quicksort.cpp,heapsort.cpp,mergesort.cpp,stdsort.cpp").split(",")

lib_folder = os.getenv("LIB_FOLDER", "libs")

# Path configuration
data_folder = os.getenv("DATA_FOLDER", "data")
input_csv_path = os.path.join(data_folder, os.getenv("DATA_CSV_FILE", "data.csv"))
output_csv_path = os.path.join(data_folder, os.getenv("OUTPUT_CSV_FILE", "output.csv"))

repeat_time = int(os.getenv("REPEAT_TIME", 10))

# Compile the data
shared_library_files = [cpp_filename[:-3] + "so" for cpp_filename in cpp_files]


os.makedirs(data_folder, exist_ok=True)
os.makedirs(lib_folder, exist_ok=True)
os.makedirs(cpp_folder, exist_ok=True)

