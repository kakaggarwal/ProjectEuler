# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def getLeader(A):
    vals = set(A)
    totalCount = 0
    numCount = 0
    threshold = len(A) // 2

    for num in vals:
        numCount = A.count(num)

        if numCount > threshold:
            return num
        else:
            totalCount += numCount

        if totalCount > threshold:
            return -1


def solution(A):
    # write your code in Python 3.6
    count = 0

    for i in range(len(A) - 1):
        first = getLeader(A[:i + 1])
        second = getLeader(A[i + 1:])

        if first == second != -1:
            count += 1

    return count


print(solution([0, 0]))
print(solution([4, 3, 4, 4, 4, 2]))
