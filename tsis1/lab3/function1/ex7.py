def has_33(): 
    listnums = [int(x) for x in input().split()]
    for i in listnums:
        if i==3:
            if listnums[listnums.index(i)+1]==3:
                print(True)
                exit(0)
    print(False)
has_33()