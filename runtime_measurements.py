import ctypes
import timeit
import time
import numpy

class BaseRuntime:
    def _prepare_data(self, data: list):
        pass
    
    def measure_runtime(self, data: list, repeat: int):
        self.data = data
        results = timeit.Timer(self._execute_sort, lambda: self._prepare_data(data), timer=time.perf_counter, globals=globals()).repeat(repeat, 1)
        return results
    
    def _execute_sort(self):
        pass

    def get_sorted_data(self):
        return list(self.args[0])

    def check_correctness(self):
        if self.get_sorted_data() != sorted(self.data):
            raise Exception("Sorting algorithm malfunctioned!")

class CppSortRuntime(BaseRuntime):
    def __init__(self, lib_path: str):
        self.lib = ctypes.CDLL(lib_path)

    def _prepare_data(self, data: list):
        arr = (ctypes.c_double * len(data))(*data)
        self.args=[arr, len(data)]
    
    def measure_runtime(self, data: list, repeat: int):
        return super().measure_runtime(data, repeat)
    
    def _execute_sort(self):
        self.lib.sort(self.args[0], self.args[1])
    
class NumpySortRuntime(BaseRuntime):
    def measure_runtime(self, data: list, repeat: int):
        return super().measure_runtime(data, repeat)

    def _prepare_data(self, data: list):
        self.args = [numpy.array(data)]
    
    def _execute_sort(self):
        self.args[0].sort()
