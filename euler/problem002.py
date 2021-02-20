# 100% score achieved

import sys

fibb = [1, 2]
evens = [2]

def getSum(n):
    sum = 0

    for num in evens:
        if num > n:
            break
        
        sum = sum + num
    
    return sum


def euler(n):
    while fibb[-1] <= n:
        newNum = fibb[-1] + fibb[-2]
        fibb.append(newNum)

        if newNum % 2 == 0:
            evens.append(newNum)

    return getSum(n)
    

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())

    print(euler(n))