#!/bin/python3

import sys


def sumSquare(n):
    sum = 0

    for i in range(1, n + 1):
        sum += i

    return sum * sum


def squareSum(n):
    sum = 0

    for i in range(1, n + 1):
        sum += i * i

    return sum


def euler(n):
    return sumSquare(n) - squareSum(n)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler(n))
