import ctypes
import timeit
import numpy

class BaseRuntime:
    def prepare_data(self, data: list):
        pass
    
    def measure_runtime(self, data: list, repeat: int):
        results = []
        for i in range(repeat):
            self.args = self.prepare_data(data)
            results += [timeit.timeit(self.execute_sort, number=1)]
        return results
    
    def execute_sort(self):
        pass

class CppSortRuntime(BaseRuntime):
    def __init__(self, lib_path: str):
        self.lib = ctypes.CDLL(lib_path)

    def prepare_data(self, data: list):
        arr = (ctypes.c_int * len(data))(*data)
        return [arr, len(data)]
    
    def measure_runtime(self, data: list, repeat: int):
        return super().measure_runtime(data, repeat)
    
    def execute_sort(self):
        self.lib.sort(self.args[0], self.args[1])
    
class NumpySortRuntime(BaseRuntime):
    def measure_runtime(self, data: list, repeat: int):
        return super().measure_runtime(data, repeat)

    def prepare_data(self, data: list):
        return [data.copy()]
    
    def execute_sort(self):
        numpy.sort(self.args[0])
