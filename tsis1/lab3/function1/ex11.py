def polindrome():
    word = str(input())
    return word == word[::-1]
if polindrome():
    print("Yes")
else:
    print("No")