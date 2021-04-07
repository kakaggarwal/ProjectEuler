__author__ = 'kakaggarwal'

import sys


def solution(N, A):
    counters = [0] * N
    maxCounter = 0
    currMax = 0

    for opr in A:
        if opr <= N:
            if maxCounter > counters[opr - 1]:
                counters[opr - 1] = maxCounter

            counters[opr - 1] += 1

            if counters[opr - 1] > currMax:
                currMax = counters[opr - 1]
        else:
            maxCounter = currMax

    for i in range(N):
        if maxCounter > counters[i]:
            counters[i] = maxCounter

    return counters


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
