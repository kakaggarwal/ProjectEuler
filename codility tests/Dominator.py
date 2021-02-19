def solution(A):
    vals = set(A)
    totalCount = 0
    numCount = 0
    threshold = len(A) / 2

    for num in vals:
        numCount = A.count(num)

        if numCount > threshold:
            return num
        else:
            totalCount += numCount

        if totalCount > threshold:
            return -1


print(solution([3, 4, 3, 2, 3, -1, 3, 3]))
