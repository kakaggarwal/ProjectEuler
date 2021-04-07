#!/bin/python3

import sys

fib = [1, 2]
evenSeq = [2]


def getEvenSum(limit, sum):
    for element in evenSeq:
        if element > limit:
            return sum
        else:
            sum += element

    return sum


def genNextFibonacci(first, second, limit, sum):
    third = first + second

    fib.append(third)

    if third % 2 == 0:
        evenSeq.append(third)

        if third <= limit:
            sum += third

    if third > limit:
        return sum
    else:
        return genNextFibonacci(second, third, limit, sum)


def euler(n):
    if max(fib) >= n:
        return getEvenSum(n, 0)
    else:
        return getEvenSum(fib[-1], 0) + genNextFibonacci(fib[-2], fib[-1], n, 0)


t = int(input("T: ").strip())

for a0 in range(t):
    n = int(input("N: ").strip())

    print(euler(n))
