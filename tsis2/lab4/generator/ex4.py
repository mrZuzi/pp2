a = int(input())
b = int(input())
def squares():
    for i in range(a, b + 1):
        yield i ** 2
list = []
for i in squares():
    list.append(str(i))
print(",".join(list))