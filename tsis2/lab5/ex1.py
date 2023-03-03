import re

a = input()
pattern = "^a(b)*$"
if re.search(pattern, a):
    print('True')
else:
    print("False")