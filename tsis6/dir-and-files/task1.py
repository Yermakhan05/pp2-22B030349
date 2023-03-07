import os

s = input("Path: ")

print("directories")
print([ans for ans in os.listdir(s) if os.path.isdir(os.path.join(s, ans))])

print("files")
print([ans for ans in os.listdir(s) if os.path.isdir(os.path.join(s, ans)) == 0])

print("files and directories")
print(os.listdir(s))