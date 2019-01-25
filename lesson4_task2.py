# Lesson 2.Task 2

from math import log2

def prime_sieve(n):
    
    lenght = int(n * log2(n)) if n > 4 else 10
        
    prime_dict = {index: True if item % 2 or item == 2 else False for index, item in enumerate(range(2, lenght + 1), 2)}
    for i in prime_dict:
        if prime_dict[i] == True:
            for j in range(i**2, lenght + 1, i):
                prime_dict[j] = False
    primes = tuple([p for p in prime_dict if prime_dict[p] == True])
    return primes[n-1]
        

def prime_simple(n):
    
    lenght = int(n * log2(n)) if n > 4 else 10
    primes = []
    for i in range(2, lenght + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)

    return primes[n-1]
    
print(prime_sieve(100))
print(prime_simple(100))
