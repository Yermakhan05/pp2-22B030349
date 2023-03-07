from functools import reduce

def multiply_list_numbers(numbers):
    product = reduce(lambda x, y: x * y, numbers)
    return product

numbers = [1, 2, 3, 4]
product = multiply_list_numbers(numbers)
print(product)