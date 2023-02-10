def prime_filter(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list
start = int(input())
end= int(input())
length = prime_filter(start, end)
if len(length) == 0:
    print("NO prime ")
else:
    print('primes are:', length)    