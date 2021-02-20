# 100% score achieved

import sys

palins = [101101]

def euler(n):
    if palins[-1] > n:
        for num in palins[::-1]:
            if num < n:
                return num
    else:
        for num in range(palins[-1] + 1, n):
            if str(num) == str(num)[::-1]:
                for div in range(102, int(num ** 0.5 + 1)):
                    if num % div == 0 and len(str(num // div)) == 3:
                        palins.append(num)

    return palins[-1]

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())

    print(euler(n))