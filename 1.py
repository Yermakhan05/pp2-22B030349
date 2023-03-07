height = int(input("Enter the height of the pyramid: "))

char = input("Which character for the top you want to use? ")

p = " "
a = height-2
b = 1
print((height-1)*p+char)
for x in range(1, height-1):
    print((a)*p+"/{}\\".format((b)*p))
    a -= 1
    b += 2

print("/{}\\".format((2*height-3)*"_"))