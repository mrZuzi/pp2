import re
def camel_to_snake(a):
    b = re.sub('([A-Z])', r'_\1', a)
    b = b.lower()
    b = re.sub('_+', '_', b)
    if b.startswith('_'):
        b = b[1:]
    return b
a =  input()
b = camel_to_snake(a)
print(b)