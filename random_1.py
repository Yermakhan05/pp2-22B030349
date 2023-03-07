import random


for x in range(4):
    x = random.randint(5, 7)
    if x == 5:
     y = random.randint(1, 16)
    elif x == 6:
     y = random.randint(1, 8)
    else:
     y = random.randint(1, 10)
    print(x, y)
