import os

def get_largest_file(dir_name):
    largest_file_path = ''
    largest_file_size = 0
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size > largest_file_size:
                largest_file_size = file_size
                largest_file_path = file_path
    if largest_file_path:
        print(f"Largest file: {largest_file_path} ({largest_file_size} bytes)")
    else:
        print("No files found in directory.")

dir_name = input("Enter directory name: ")
if os.path.isdir(dir_name):
    get_largest_file(dir_name)
else:
    print("Invalid directory name.")
