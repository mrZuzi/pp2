n = int(input())
a = [i for i in range(0, n+1)]
b = [i for i in a if i%2 == 0]
print(b)

def even_num(n):
    for i in range(0, n+1, 2):
        yield str(i)
n = int(input("Enter number: "))
even_num = even_num(n)
result = ','.join(even_num)
print(result)



# n= int(input())
# list = list(range(0,9))
# print(list[0::2])