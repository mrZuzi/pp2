def toString(List):
     return ''.join(List)

def permute(s, n, r):
    if n == r:
        print(toString(s))
    else:
        for i in range(n, r):
            s[n], s[i] = s[i], s[n]
            permute(s, n+1, r)
            s[n], s[i] = s[i], s[n] 

string = input(str)
r = len(string)
s = list(string)
permute(s, 0, r) 
    
    
    