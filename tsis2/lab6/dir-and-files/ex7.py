path1 = input("Enter first path: ")
path2 = input("Enter second path: ")
with open(path1, "r") as s, open(path2, "w") as d:
    contents = s.read()
    d.write(contents)
print("File copied successfully!")
