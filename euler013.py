import sys


def euler(numbers):
    res = ''
    carry = 0

    for i in range(50):
        temp = carry

        for number in numbers:
            temp += int(number[-1-i])

        carry = int((temp - (temp % 10)) / 10)
        res = str(temp % 10) + res

    res = str(carry) + res

    return str(res)[0:10]


t = int(input().strip())
numbers = []

for a0 in range(t):
    numbers.append(input().strip())

print(euler(numbers))
