import os
from settings import cpp_folder, cpp_files, lib_folder, shared_library_files
import shutil

shutil.rmtree(lib_folder, ignore_errors=True)
os.mkdir(lib_folder)

for cpp_filename, shared_lib_filename in zip(cpp_files, shared_library_files):
    compile_command = f"g++ -shared -fPIC -o {lib_folder}/{shared_lib_filename} {cpp_folder}/{cpp_filename}"
    os.system(compile_command)
