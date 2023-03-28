only_ints = []
list_of_string = []
float_nums = []
array_of_bools = []


arr2 = [100, "Astana", -10, 1, 10.4, True, 3, 4, 70, 24, -9, "Almaty", "Aktau"]
for element in arr2:
    if "int" in str(type(element)):
        only_ints.append(element)
    elif "str" in str(type(element)):
        list_of_string.append(element)
    elif "float" in str(type(element)):
        float_nums.append(element)
    elif "bool" in str(type(element)):
        array_of_bools.append(element)

print(only_ints)
print(list_of_string)
print(float_nums)
print(array_of_bools)
     
