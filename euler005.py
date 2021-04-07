#!/bin/python3

import sys


def getProduct(numbers):
    prod = 1
    i = 0

    while i < len(numbers):
        j = len(numbers) - 1
        prod *= numbers[i]

        while j >= 0:
            if (numbers[j] != 1 and numbers[i] != 1 and numbers[j] % numbers[i] == 0):
                numbers[j] = int(numbers[j] / numbers[i])
            j -= 1
        i += 1
    return prod


def euler(n):
    if n == 1:
        return n
    else:
        return getProduct(list(range(2, n + 1)))


t = int(input("t:").strip())
for a0 in range(t):
    n = int(input("n:").strip())
    print(euler(n))
