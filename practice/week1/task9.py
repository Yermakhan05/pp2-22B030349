n = int(input())

mytuple = {}
mytuple_count = {}

for i in range(0, n):
    name, point = input().split()
    point = int(point)
    if name in mytuple:
        mytuple[name] += point
        mytuple_count[name] += 1
    else:
        mytuple[name] = point
        mytuple_count[name] = 1

for name in mytuple:
    mytuple[name] /= mytuple_count[name]
    print(name, int(mytuple[name]))