#!/bin/python3

import sys
from datetime import datetime

chains = [0] * 10000000
chains[1] = 1


def getChainCount(n):
    try:
        # if n > 5000000:
        #     if n % 2 == 0:
        #         n = int(n / 2)
        #     else:
        #         n = 3 * n + 1

        #     return 1 + getChainCount(n)

        if chains[n] != 0:
            return chains[n]

        orign = n

        if n % 2 == 0:
            n = int(n / 2)
            chains[orign] = 1 + getChainCount(n)
        else:
            n = 3 * n + 1
            chains[orign] = 1 + getChainCount(n)

        return chains[orign]
    except Exception as err:
        print(err)


def euler(n):
    max = 0
    index = 0

    for i in range(n, int(n / 2), -1):
        if chains[i] == 0:
            getChainCount(i)

        if chains[i] > max:
            max = chains[i]
            index = i

    return index


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    print(datetime.now())
    print(euler(n))
    print(datetime.now())
