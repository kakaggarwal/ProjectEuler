import sys


def euler(n):
    if n < 4:
        return 3

    while n >= 4:
        remainders = []

        for i in range(n - 1):
            if i == 0:


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    print(euler(n - 1))
