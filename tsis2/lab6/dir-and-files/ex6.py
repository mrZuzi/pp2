import string
l = list(string.ascii_uppercase)
for letter in l:
    n = letter + ".txt"
    with open(n, "w") as file:
        file.write("This is file " + n)