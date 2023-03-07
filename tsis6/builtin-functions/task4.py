import time
import math

def calculate_square_root(number):
    return math.sqrt(number)

number = int(input())
milliseconds = int(input())


result = calculate_square_root(number)

print("The square root of", number, "after", milliseconds, "milliseconds is", result)