#!/bin/python3

import sys

def getMultiplesSum(n, val):
    d = n // val

    return ((1 + d) * d * val) // 2

def euler(n):
    return getMultiplesSum(n, 3) + getMultiplesSum(n, 5) - getMultiplesSum(n, 15)


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())

    print(euler(n - 1))
