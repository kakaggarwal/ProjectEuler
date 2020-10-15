import sys

amicables = {220, 284}


def sumOfFactors(num):
    sum = 1

    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            sum += i

            if i != num / i:
                sum += num / i

    return int(sum)


def getAmicable(n):
    a = max(amicables)

    while a < n:
        a += 1
        b = sumOfFactors(a)

        if sumOfFactors(b) == a:
            amicables.add(a)
            amicables.add(b)


def getSum(n):
    sum = 0

    for i in sorted(amicables):
        if i < n:
            sum += i
        else:
            break

    return sum


def euler(n):
    if max(amicables) <= n:
        getAmicable(n)

    return getSum(n)


euler(100000)

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    print(euler(n))
