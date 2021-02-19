#!/bin/python3

import sys

def getMultiplesSum(n):
    sum = 0

    for num in range(n - 1, 2, -1):
        if num % 3 == 0 or num % 5 == 0:
            sum = sum + num
    
    return sum


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())

    print(getMultiplesSum(n))
