nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
nums=list(filter(lambda x: x!=1,nums))
is_prime = lambda number: all( number%i != 0 for i in range(2, int(number**.5)+1) )
primes=list(filter(is_prime,nums))
print(primes)