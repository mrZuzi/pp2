import os

l = input().split()
with open('test.txt','w') as f:
    for i in l:
        f.write(i + '\n')
        
    