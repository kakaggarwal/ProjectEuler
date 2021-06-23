import sys


def getScore(name):
    score = 0

    for ch in name:
        score += ord(ch) - 64

    score *= names.index(name) + 1

    return score


n = int(input().strip())
names = [] * n

for a0 in range(n):
    names.append(input().strip().upper())

names = sorted(names)
qNum = int(input().strip())

for a1 in range(qNum):
    q = input().strip().upper()
    print(getScore(q))
