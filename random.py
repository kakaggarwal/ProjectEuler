import sys

# for s in range(1, 450):
#     if s * (s - 900) == -180000:
#         print(s)


def getFactorCount(number):
    if number % 2 == 0 and number > 2:
        number = number / 2
        count = 4
    else:
        count = 2

    divisor = 3

    while divisor < number // 2:
        if number % divisor == 0:
            number = number / divisor
            count += 2
            divisor = 3

        divisor += 2

    return count


limit = 10000
triads = [0] * limit
fCounts = [0] * limit
triads[0] = fCounts[0] = 0
triads[1] = fCounts[1] = 1

for i in range(2, len(triads)):
    triads[i] = triads[i - 1] + i
    fCounts[i] = getFactorCount(triads[i])

print(max(fCounts))
