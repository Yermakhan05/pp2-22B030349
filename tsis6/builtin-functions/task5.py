def thistuple_true(mytuple):

    return all(mytuple)


mytuple = ("tuple", True, 36, False)
print(mytuple)
if thistuple_true(mytuple):
    print("All elements are True!")
else:
    print("Elements are not True!")   