import os

current_dir = "C:/"

while True:
    user_input = input(current_dir + "> ")
    command = user_input.split()[0]
    args = user_input.split()[1:]
    
    if command == "ls" or command == "dir":
        print("\n".join(os.listdir(current_dir)))
        
    elif command == "cd":
        if args[0] == "..":
            current_dir = os.path.dirname(current_dir)
        else:
            new_dir = os.path.join(current_dir, args[0])
            if os.path.isdir(new_dir):
                current_dir = new_dir
            else:
                print("Exception: Directory not found")
                
    elif command == "mkdir":
        new_dir = os.path.join(current_dir, args[0])
        os.mkdir(new_dir)
        
    elif command == "rmdir":
        dir_to_delete = os.path.join(current_dir, args[0])
        os.rmdir(dir_to_delete)
        
    elif command == "touch":
        new_file = os.path.join(current_dir, args[0])
        with open(new_file, 'w') as f:
            pass
        
    elif command == "rm":
        file_to_delete = os.path.join(current_dir, args[0])
        os.remove(file_to_delete)
        
    elif command == "cat":
        file_to_read = os.path.join(current_dir, args[0])
        with open(file_to_read, 'r') as f:
            print(f.read())
            
    else:
        print("Invalid command")
