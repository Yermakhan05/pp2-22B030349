def sqaure(i):
    return i * i

A, B = input().split()
a = int(A)
b = int(B)

for i in range(a, b+1, 1):
    print(sqaure(i))