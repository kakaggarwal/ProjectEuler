#!/bin/python3

import sys
from datetime import datetime

primes = [2, 3]
triangles = [0, 1]
factCounts = [1, 3]


def getFactorCount(num):
    counter = 2
    k = 0
    div = primes[k]

    while div <= num ** 0.5:
        if num % div == 0:
            num = num / div
            counter += 2

            if div > primes[-1]:
                primes.append(div)
        else:
            if div < primes[-1]:
                k += 1
                div = primes[k]
            else:
                div += 2

    if num == div:
        counter += 1

    return counter


def calculateFactCounts(i, n):
    while True:
        triangles.append(i + triangles[i - 1])
        counter = getFactorCount(triangles[i])

        if counter > len(factCounts):
            factCounts.extend([triangles[i]] * (counter - len(factCounts)))

        if counter > n:
            return factCounts[n]

        i = len(triangles)


def euler(n):
    if len(factCounts) > n:
        return factCounts[n]
    else:
        return calculateFactCounts(len(triangles), n)


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    print(datetime.now())
    print(euler(n))
    print(datetime.now())
