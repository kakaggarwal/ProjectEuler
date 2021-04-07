import sys

abundants = [12]


def getAbundants():
    for i in range(18, 28112):
        if getFactorsSum(i) > i:
            abundants.append(i)


def getFactorsSum(num):
    sum = 1
    div = 2

    while div <= num ** 0.5:
        if num % div == 0:
            sum += div

            if num // div != div:
                sum += num // div

            if sum > num:
                break

        div += 1

    return sum


def euler(n):
    if n > 28123:
        return 'YES'

    if n < 24:
        return 'NO'

    for i in abundants:
        if i > (n - 12):
            break

        if (n - i) in abundants:
            return 'YES'

    return 'NO'


getAbundants()

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    print(euler(n))
