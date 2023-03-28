s = input("File name: ")

file = open(s, "r")

cnt = 0
for i in file:
    cnt += 1

print(cnt)