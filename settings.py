import os
from runtime_measurements import CppSortRuntime, NumpySortRuntime

# The names of the sorting algorithms, use for header of csv report
sorting_algorithm_names = os.getenv("SORTING_ALGORITHM_NAMES", "Quick Sort,Heap Sort,Merge Sort,std::sort,Numpy Sort").split(",")

# The filenames of the shared libraries that contain the sorting algorithms in cpp
cpp_folder = os.getenv("CPP_FOLDER", "sorting_algorithms")
cpp_files = os.getenv("CPP_FILENAMES", "quicksort.cpp,heapsort.cpp,mergesort.cpp,stdsort.cpp").split(",")

lib_folder = os.getenv("LIB_FOLDER", "libs")

# Path config
data_folder = os.getenv("DATA_FOLDER", "data")
input_csv_path = os.path.join(data_folder, os.getenv("DATA_CSV_FILE", "data.csv"))
output_csv_path = os.path.join(data_folder, os.getenv("OUTPUT_CSV_FILE", "output.csv"))

# Compile the data
shared_library_files = [cpp_filename[:-3] + "so" for cpp_filename in cpp_files]
runtime_configs = list(zip(sorting_algorithm_names, [CppSortRuntime(f"libs/{shared_lib_filename}") for shared_lib_filename in shared_library_files] + [NumpySortRuntime()]))