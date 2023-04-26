my_dict = {}
command, key, value = '', '', ''

while True:
    print("What do you want to do: add/delete/exit?")
    command = input()
    if command == 'exit': break
    print("Enter the key:")
    key = input()
    if command == 'delete':
        my_dict.pop(key)
    elif command == 'add':
        print("Enter the value:")
        value = input()
        my_dict[key] = value
    print("here is dictionary:")
    for k in my_dict:
        print("        -{}:{}".format(k, my_dict[k]))