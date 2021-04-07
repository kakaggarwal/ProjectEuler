#!/bin/python3

import sys


def oddNumber(n):
    divisor = 3

    while divisor <= int(n ** 0.5):
        if n % divisor == 0:
            n = n // divisor
            divisor = 3
        else:
            divisor += 2

    if n > 2:
        return n
    else:
        return divisor


def euler(n):
    while n % 2 == 0:
        n = n // 2

    if n == 1:
        return 2

    return oddNumber(n)


t = int(input("T: ").strip())

for a0 in range(t):
    n = int(input("N: ").strip())

    print(euler(n))