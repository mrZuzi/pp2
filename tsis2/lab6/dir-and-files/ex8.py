import os
path = input("Enter path: ")
if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted successfully")
    else:
        print("You don't have permission to delete the file")
else:
    print("File does not exist!")