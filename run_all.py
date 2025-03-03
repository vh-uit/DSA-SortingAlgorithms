import subprocess

def run_script(script_name):
    print(f"Starting {script_name}...")
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_name}: {result.stderr}")
    else:
        print(f"Output of {script_name}: {result.stdout}")
    print(f"Finished {script_name} with return code {result.returncode}")

if __name__ == "__main__":
    scripts = ['generate_data.py', 'compile_libraries.py', 'run_analysis.py']
    for script in scripts:
        run_script(script)