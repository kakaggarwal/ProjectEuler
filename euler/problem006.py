# 100% score achieved

import sys

def euler(n):
    a = (n * (n + 1)) // 2
    
    return a ** 2 - ((a * ((2 * n) + 1)) // 3)

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())

    print(euler(n))