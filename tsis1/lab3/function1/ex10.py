def nodup():
    list1 = [str(x) for x in input().split()]
    x = []
    for i in list1:
        if i not in x:
            x.insert(i)
    print(x)
nodup()
        