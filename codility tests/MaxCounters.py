import sys


def solution(N, A):
    counters = [0] * N

    for opr in A:
        if 1 <= opr and opr <= N:
            counters[opr - 1] += 1
        elif opr == N + 1:
            counters = [max(counters)] * N

    return counters


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
