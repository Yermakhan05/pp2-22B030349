file_name = input("File name: ")

file = open(file_name, 'r')

new_file = input("new file name: ")
file2 = open(new_file, 'w')

file2.write(file.read)