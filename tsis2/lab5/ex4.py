import re
a = input("Enter text: ")
matches = re.findall(r'[A-Z][a-z]+', a)
print(matches)
