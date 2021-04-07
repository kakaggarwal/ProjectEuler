def solution(A):
    lenA = len(A)
    maxSum = 0

    for x in range(lenA - 2):
        for y in range(x + 1, lenA - 1):
            for z in range(y + 1, lenA):
                sliceSum = sum(A[x + 1:y]) + sum(A[y + 1:z])
                maxSum = max(sliceSum, maxSum)

    return maxSum

print(solution([3, 2, 6, -1, 4, 5, -1, 2]))
