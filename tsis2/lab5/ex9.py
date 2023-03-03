import re
def spaces(a):
    valid = r'(?<!^)(?=[A-Z])'
    a = re.sub(valid, ' ', a)
    return a
a = input()
a = spaces(a)
print(a)