import math


def solution(N):
    factors = {1, N}

    for num in range(2, math.ceil(N ** 0.5) + 1):
        if N % num == 0:
            if num in factors:
                return len(factors)
            else:
                factors.update([num, N // num])

    return len(factors)


# print(solution(24))
print(solution(16))
