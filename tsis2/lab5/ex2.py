import re
a = input()
b = re.findall(r"ab{2,3}", a)
if b:
    print("YES")
else:
    print("NO")