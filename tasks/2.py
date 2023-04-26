import random
x = random.randint(a=8, b=10)
if x==8:
    y = random.randint(1, 8)
elif x == 9:
    y = random.randint(1, 5)
else:
    y = random.randint(1, 7)

print(x, y)