my_list = []
print("Here is the list:")
while True:
    for i in my_list:
        print("        - "+i)
    print("\nWhat do you want to add:")
    x = input()
    if x == "nothing":
        print("\nHere is the list:")
        for i in my_list:
            print("        - "+i)
        break
    my_list.append(x)
    print("\nHere is the list:")
    

print("\nGoodbye")