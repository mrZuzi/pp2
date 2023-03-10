def f(x):
    if x == "True": return True
    return False

def alltrue():
    list = [f(x) for x in input().split(',')]
    tuple1 = tuple(list)
    return(all(tuple1))

print(alltrue())

