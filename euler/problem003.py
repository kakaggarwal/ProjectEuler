# 100% score achieved

import sys


def euler(n):
    while n % 2 == 0:
        n = n // 2
    
    if n == 1:
        return 2

    num = 3

    while num <= int(n ** 0.5):
        if n % num == 0:
            n = n // num
        else:
            num += 2
    
    if n > 1:
        return n
    else:
        return num

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())

    print(euler(n))