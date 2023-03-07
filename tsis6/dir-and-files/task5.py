mylist = input().split()

file_name = input("file name: ")

file = open(file_name, 'w')

for element in mylist:
    file.write(element+' ')