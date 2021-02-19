def solution(A):
    maxSum = A[0]

    for P in range(len(A)):
        for Q in range(P, len(A)):
            sliceSum = sum(A[P:Q + 1])
            maxSum = max(sliceSum, maxSum)

    return maxSum


print(solution([3, 2, -6, 4, 0]))
