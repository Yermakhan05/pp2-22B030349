def prime(n):
    for i in range(2, n, 1):
        if n % i == 0:
            return False
    return True

numbers = input().split()
prime_numbers = list(filter(lambda x: prime(int(x)), numbers))
print(prime_numbers)