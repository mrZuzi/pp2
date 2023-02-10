def histogram():
    list1 = [int(x) for x in input().split()]
    for x in list1:
        sign = ''
        sign1 = x
        while sign1 != 0 :
            sign += '*'
            sign1-=1
        print(sign)
histogram()