import os
path = input("Enter path: ")
directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
print("Directories in path:")
print(directories)
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
print("Files in path:")
print(files)
all = os.listdir(path)
print("All contents in path:")
print(all)