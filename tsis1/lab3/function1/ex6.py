def reverse_sentence(s):
    s = s.split()
    s.reverse()
    return ' '.join(s)
s = input(str)
print(reverse_sentence(s))
