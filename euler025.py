import sys
import math


def euler(n):
    return math.ceil(4.78497 * n - 3.1127)


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    print(euler(n))
