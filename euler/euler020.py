import sys

factorials = [1, 1]


def getSumofDigits(num):
    sum = 0

    for i in str(num):
        sum += int(i)

    return sum


def factorial(n):
    if n >= len(factorials):
        factorials.append(n * factorial(n - 1))

    return factorials[n]


def euler(n):
    return getSumofDigits(factorial(n))


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    print(euler(n))
