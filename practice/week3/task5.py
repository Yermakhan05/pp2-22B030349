my_list = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
 
count_floats = lambda flt: len([i for i in flt if type(i) == float])

count_floats = count_floats(my_list)
print("Result:", count_floats)