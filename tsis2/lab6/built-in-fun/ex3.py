def polindrome ():
    str = input().casefold()
    str2 = str[::-1]
    print(str2)
    if str == str2:
        print("YES")
    else:
        print("NO")
polindrome()