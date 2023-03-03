import re
v = input()
q = re.sub( "[ ,.]", ":" , v )
print(q)