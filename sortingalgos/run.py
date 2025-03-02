import ctypes
import os
import random
import timeit
import numpy
cpp_filenames = ["quicksort.cpp","heapsort.cpp", "mergesort.cpp", "stdsort.cpp"]
shared_lib_filenames = [cpp_filename[:-3] + "so" for cpp_filename in cpp_filenames]

my_list = [random.randint(1, 10000) for _ in range(100000)]
for cpp_filename, shared_lib_filename in zip(cpp_filenames, shared_lib_filenames):
    compile_command = f"g++ -shared -fPIC -o {shared_lib_filename} {cpp_filename}"
    os.system(compile_command)

for shared_lib_filename in shared_lib_filenames:
    print(shared_lib_filename)
    for i in range(10):
        lib = ctypes.CDLL("/workspaces/DSA-SortingAlgorithms/sortingalgos/"+shared_lib_filename)

        c_array_type = ctypes.c_int * len(my_list)
        c_array = c_array_type(*my_list)

        print(timeit.repeat(lambda: lib.sort(c_array, len(my_list)), number=1))

    os.remove(shared_lib_filename)

print("numpy")
for i in range(10):
    array = my_list.copy()
    print(timeit.timeit(lambda: numpy.sort(array), number=1))
