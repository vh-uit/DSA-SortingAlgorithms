# DSA-SortingAlgorithms

This project is designed to measure and compare the runtime performance of different sorting algorithms implemented in both C++ and Python (using NumPy). The results are read from a CSV file, processed, and then written to an output CSV file.

## Files and Directories

### `runtime_measurements.py`
- **BaseRuntime**: An abstract base class that defines the structure for measuring runtime. It includes methods for preparing data, measuring runtime, and executing the sort.
- **CppSortRuntime**: Inherits from `BaseRuntime` and is used to measure the runtime of C++ sorting algorithms. It loads the shared library, prepares the data, and executes the sort using the C++ function.
- **NumpySortRuntime**: Inherits from `BaseRuntime` and is used to measure the runtime of NumPy's sort function. It prepares the data and executes the sort using NumPy.

### `run_analysis.py`
- Reads input data from a CSV file.
- Configures runtime measurement for different sorting algorithms.
- Measures the runtime for each algorithm on the input data.
- Writes the results to an output CSV file.

### `settings.py`
- Configures environment variables and paths for the project.
- Defines sorting algorithm names, C++ filenames, and shared library files.
- Ensures necessary directories exist.

### `compile_libraries.py`
- Compiles C++ source files into shared libraries.
- Cleans up the library directory and recompiles the shared libraries.

### `.env.example` and `.env`
- Example and actual environment configuration files.
- Define environment variables for sorting algorithm names, C++ folder and filenames, library folder, and data folder paths.

## Usage

1. **Setup Environment**: Copy `.env.example` to `.env` and modify as needed.
2. **Compile Libraries**: Run `compile_libraries.py` to compile the C++ sorting algorithms into shared libraries.
3. **Run Analysis**: Execute `run_analysis.py` to measure and compare the runtime of the sorting algorithms. The results will be written to the output CSV file specified in the settings.

## Dependencies

- Python packages: `ctypes`, `timeit`, `numpy`, `csv`, `os`, `shutil`
- C++ compiler: `g++`

## Notes

- Ensure that the C++ source files and the data CSV file are correctly placed as per the paths defined in the environment variables.
- The project assumes that the C++ sorting functions are defined in the shared libraries and follow a specific signature for sorting.
