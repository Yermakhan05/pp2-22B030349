def ounces(grams):
    return 28.349523*grams

grams = int(input("gram: "))
print("ounces: {}".format(ounces(grams)))