import math
def filter_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1, 1):
        if x % i == 0:
            return False
    return True

n = int(input())
a = input().split()

for i in range(0, n, 1):
    a[i] = int(a[i])
    if filter_prime(a[i]) == True:
        print(a[i])