#!/bin/python3

import sys

primes = [2, 3]


def findPrime(mayBePrime):
    for divisor in primes:
        if divisor >= (mayBePrime // 2):
            primes.append(mayBePrime)
            return True

        if mayBePrime % divisor == 0:
            findPrime(mayBePrime + 2)
            return False


def euler(n):
    if n <= len(primes):
        return primes[n - 1]
    else:
        while len(primes) < n:
            findPrime(max(primes) + 2)

        return max(primes)


t = int(input("Enter T: ").strip())

for a0 in range(t):
    n = int(input("Enter N: ").strip())

    print(euler(n))
