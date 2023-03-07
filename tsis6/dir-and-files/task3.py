import os

s = input("Path: ")

if os.path.exists(s):
    print("Path exists")

    filename = os.path.basename(s)
    directory = os.path.dirname(s)

    print("Filename:", filename)
    print("Directory:", directory)
else:
    print("Path does not exist")