import os
import shutil

# Get directory path from user
dir_path = input("Enter the directory path: ")

# Dictionary to store file types and corresponding subdirectories
file_types = {
    '.txt': 'txt',
    '.pdf': 'pdf',
    '.jpg': 'jpg',
    '.jpeg': 'jpg',
    '.png': 'png',
    # add more file types and subdirectories as needed
}

# Iterate over files in directory
for filename in os.listdir(dir_path):
    file_path = os.path.join(dir_path, filename)
    
    # Get file extension
    extension = os.path.splitext(filename)[1].lower()
    
    # Check if file extension is in dictionary
    if extension in file_types:
        # Get subdirectory name for file type
        subdirectory = file_types[extension]
        
        # Create subdirectory if it doesn't exist
        if not os.path.exists(os.path.join(dir_path, subdirectory)):
            os.mkdir(os.path.join(dir_path, subdirectory))
        
        # Move file to subdirectory
        shutil.move(file_path, os.path.join(dir_path, subdirectory))
        
# Print message
print("Files have been organized!")
