import re
a = input()
matches = re.findall("a.+b$", a)
print(matches)