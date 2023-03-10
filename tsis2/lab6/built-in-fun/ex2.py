def upper_lower ():
    str = input()
    cnt =   {"UPPER_CASE":0, "lower_case":0}
    for i in str:
        if i.isupper():
            cnt["UPPER_CASE"]+=1
        elif i.islower():
            cnt["lower_case"]=+1
    print(cnt)
upper_lower()