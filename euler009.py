#!/bin/python3

import sys
import math

pn = dict()


def divisors(n):
    for divisor in range(1, int(n**0.5) + 1):
        if n % divisor == 0:
            yield divisor, n // divisor


for r in range(2, 550, 2):
    st = r*r // 2

    for s, t in divisors(st):
        x = (r+s) + (r+t) + (r+s+t)
        pn[x] = (r+s) * (r+t) * (r+s+t)


def euler(n):
    if n in pn:
        return pn[n]
    else:
        return -1


t = int(input("T: ").strip())

for a0 in range(t):
    n = int(input("N: ").strip())

    print(euler(n))
