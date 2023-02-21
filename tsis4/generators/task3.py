def generator(n):
    numbers = [i for i in range(0, n+1, 1) if i % 4 == 0 or i % 3 == 0]
    return numbers

n = int(input())
print(generator(n))
