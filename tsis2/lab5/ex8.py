import re
a = input()
b = re.findall('[A-Z][^A-Z]*', a)
print(b)