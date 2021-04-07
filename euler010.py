#!/bin/python3

import sys
from datetime import datetime

limit = 1000001
sums = [0] * limit
primes = [True] * limit
primes[0] = primes[1] = False

for i, isprime in enumerate(primes):
    if isprime:
        sums[i] = sums[i-1] + i

        for j in range(i*i, limit, i):
            primes[j] = False
    else:
        sums[i] = sums[i-1]


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sums[n])
