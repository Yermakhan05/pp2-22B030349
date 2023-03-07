import os

s = input("Path: ")

if os.access(s, os.F_OK):
    print("Path exists")
else:
    print("Path does not exist")

if os.access(s, os.R_OK):
    print("Path is readable")
else:
    print("Path is not readable")

if os.access(s, os.W_OK):
    print("Path is writable")
else:
    print("Path is not writable")

if os.access(s, os.X_OK):
    print("Path is executable")
else:
    print("Path is not executable")