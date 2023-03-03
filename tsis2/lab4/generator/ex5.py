n = int(input())
def down():
    cnt = 0
    while cnt <= n:
        if n == 0:
            yield 0
            break
        else:
            yield n - cnt
            cnt += 1
list = []
for i in down():
    list.append(str(i))
print(",".join(list))