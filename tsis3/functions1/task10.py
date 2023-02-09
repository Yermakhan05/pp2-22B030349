def unique(l):
    for i in range(len(l) - 1):
       cnt = 0
       for j in range(i + 1, len(l)):
            if l[i] == "":
                break
            if l[i] == l[j]:
                l[j] = ""
    return [x for x in l if x != ""]


fruits = ["apple", "banana", "cherry", "apple", "cherry", "orange", "banana"]
print(unique(fruits))