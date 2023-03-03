import re
a = input()
valid = r'[a-z]+_[a-z]+'
matches = re.findall(valid, a)
print("Matches found:")
for match in matches:
    print(match)