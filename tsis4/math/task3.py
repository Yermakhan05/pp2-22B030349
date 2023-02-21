import math

n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))
Area = math.floor(area)
print("The area of the polygon is: "+Area)