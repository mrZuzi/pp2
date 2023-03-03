import re
a = input()
def snake_to_camel(l):
    v = re.findall("[a-z]+", a)
    h = ""
    for i in v:
        h += i[0].upper() + i[1 : len(i)]
    return h
print(snake_to_camel(a))