import os

# function to read file and return the maximum value for a given name
def get_max_value(file_name, name):
    max_value = -1
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip().split()
            if line[0] == name:
                value = int(line[1])
                if value > max_value:
                    max_value = value
    return max_value

# accept input file names separated by space
input_files = input("Enter input file names separated by space: ").split()

# if no file names are provided, use default file names
if not input_files:
    input_files = ['file1.txt', 'file2.txt', 'file3.txt']

# check if all input files have .txt extension
for file in input_files:
    if not file.endswith('.txt'):
        raise ValueError("Invalid file format. Only .txt files are allowed.")

# find the maximum value for the given name in each file
max_values = []
name = input("Enter name to find maximum value for: ")
for file in input_files:
    if os.path.isfile(file):
        max_value = get_max_value(file, name)
        max_values.append(max_value)
        print(f"Maximum value for '{name}' in '{file}' is {max_value}.")
    else:
        max_values.append(-1)
        print(f"'{file}' not found. Skipping...")

# print the maximum value among all files
if max_values:
    max_value = max(max_values)
    if max_value == -1:
        print(f"No name '{name}' found in any file.")
    else:
        print(f"Maximum value for '{name}' among all files is {max_value}.")
else:
    print("No input files provided.")
