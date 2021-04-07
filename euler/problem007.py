# 100% score achieved

import sys

primes = [2, 3, 5, 7, 11, 13]

def euler(n):
    num = primes[-1]

    while len(primes) < n:
        num += 2

        for div in primes:
            if div > int(num ** 0.5):
                primes.append(num)
                break
            elif num % div == 0:
                break
    
    return primes[n - 1]

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())

    print(euler(n))