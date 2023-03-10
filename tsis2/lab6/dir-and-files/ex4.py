import os

cnt = 0
with open('test.txt', 'r') as f:
    for lines in f:
        cnt+=1
print(cnt)

