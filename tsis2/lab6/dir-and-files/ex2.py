import os
path = input("Enter path to checking: ")
if os.path.exists(path):
    print(f"{path} exist")
    if os.access(path, os.R_OK):
        print(f"r{path} readable")
    else:
        print(f"{path} not readable")
    if os.access(path, os.W_OK):
        print(f"{path} writable")
    else:
        print(f"{path} not writable")
    if os.access(path, os.X_OK):
        print(f"{path} executable")
    else:
        print(f"{path} not executable")
else:
    print(f"{path} doesn't exist!")
