adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
Mylist = [0, 0, 0]
for y in range(0, 3, 1):
    for x in adj:
        if (x == "tasty" and y == 2):
            continue
        elif x == "big":
            pass
        else:
           print(x, fruits[y])
           Mylist[y] += 1

y = 0
for x in Mylist:
    print(fruits[y], x)
    y += 1