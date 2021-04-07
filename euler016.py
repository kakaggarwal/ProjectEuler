import sys


def euler(n):
    num = str(2 ** n)
    sum = 0

    for i in num:
        sum += int(i)

    return sum


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())

    print(euler(n))
