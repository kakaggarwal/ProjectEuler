#!/bin/python3

import sys


def euler(num, k):
    max = 0
    strNum = list(str(num))
    while len(strNum) >= k:
        prod = 1

        for i in range(k):
            prod *= int(strNum[i])

        if prod > max:
            max = prod

        del strNum[0]

    return max


t = int(input("t:").strip())
for a0 in range(t):
    n, k = input("n,k:").strip().split(' ')
    n, k = [int(n), int(k)]
    num = input("num:").strip()

    print(euler(num, k))
