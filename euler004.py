#!/bin/python3

import sys


def euler(n):
    for number in range(n - 1, 101100, -1):
        if str(number) == str(number)[::-1]:
            for root in range(100, int(number ** 0.5 + 1)):
                if (number % root == 0 and number / root < 999):
                    return number


t = int(input("t:").strip())

for a0 in range(t):
    n = int(input("n:").strip())
    print(euler(n))
