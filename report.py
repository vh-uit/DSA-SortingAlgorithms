import pandas as pd
import ast
import matplotlib.pyplot as plt
import glob
import random

# Load the CSV data from all files starting with 'output' in the data folder
file_paths = glob.glob('data/output*.csv')
df_list = [pd.read_csv(file_path) for file_path in file_paths]
df = pd.concat(df_list, ignore_index=True)

# Convert the Runtime string to a list of floats
df['Runtime'] = df['Runtime'].apply(ast.literal_eval)

# Function to plot multiple columns graph
def plot_multiple_columns(df):
    algorithms = df['Algorithm'].unique()
    data_sets = df['Data set #'].unique()
    avg_runtimes = {data_set: [] for data_set in data_sets}
    avg_table = pd.DataFrame(index=algorithms, columns=data_sets)

    for data_set in data_sets:
        for algorithm in algorithms:
            subset = df[(df['Algorithm'] == algorithm) & (df['Data set #'] == data_set)]
            if not subset.empty:
                avg_runtime = subset['Runtime'].apply(lambda x: sum(x) / len(x)).mean()
                avg_runtimes[data_set].append(avg_runtime)
                avg_table.at[algorithm, data_set] = avg_runtime
            else:
                avg_runtimes[data_set].append(0)
                avg_table.at[algorithm, data_set] = 0

    bar_width = 0.05  # Smaller bar width
    index = range(len(algorithms))
    plt.figure(figsize=(12, 8))

    for i, data_set in enumerate(data_sets):
        if data_set == 0:
            color = 'darkgreen'
        elif data_set == 1:
            color = 'darkred'
        elif 2 <= data_set <= 9:
            color_intensity = 0.1 + (data_set - 2) * 0.1
            color = (0, 0.4 - color_intensity*0.4, 1 - color_intensity*0.9, 1) 
        plt.bar([p + bar_width * i for p in index], avg_runtimes[data_set], width=bar_width, label=f'Data set {data_set}', color=color)

    plt.xlabel('Algorithm')
    plt.ylabel('Average Runtime (s)')
    plt.title('Average Runtime per Data set and Algorithm')
    plt.xticks([p + bar_width * (len(data_sets) / 2) for p in index], algorithms)
    plt.legend()
    plt.tight_layout()
    plt.savefig('charts/multiple_columns_swapped.png')
    plt.close()

    # Save the average table to a CSV file
    avg_table.to_csv('charts/average_runtime_table.csv')

# Plot the multiple columns graph
plot_multiple_columns(df)
