cars = ["Toyota", "BMW", "Mercedes", "Audi", "Lexus"]
cars.pop()                       # pop
cars.append("BMW")              # append
cars.remove("Mercedes")        # remove
print(cars)
print(cars.count("BMW"))
array = [1, 2, 3, 4, 4, 4, 4, 5]
x = array.count(4)           # count
print(x)                  
array.clear()               #clear
x = cars.copy()             #copy
print(x)
x.extend(cars)             #extend
print(x)
print(x.index("BMW")+1)   # index
cars.insert(0, "Volvo")  # insert
print(cars)
cars.reverse()         # reverse
print(cars)
cars.sort(reverse=True)           # sort
print(cars)
def Myfunc(e):
    return e['year']
Cars = []
for x in cars:
    year = input("Year is {}? ".format(x))
    car = {'car':x, 'year': year}
    Cars.append(car)
Cars.sort(key=Myfunc)
for x in Cars:
    print(x['car'], x['year'])
       
