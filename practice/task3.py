print("введи число:")
numbers = set(input().split())
runing = True
while runing:
    comand, *args = input("Введи команду: ").split()
    if comand == "pop":
        numbers.pop()
    elif comand == "remove":
        numbers.remove(args[0])
    elif comand == "discard":
        numbers.discard(args[0])
    elif comand == "print":
        print(numbers)
    elif comand == "stop":
        runing = False
        break
    else:
        print("введи правилну команду")
    
print("Пока.")
