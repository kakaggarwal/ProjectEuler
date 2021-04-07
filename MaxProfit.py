def solution(A):
    maxProfit = 0

    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            maxProfit = max(maxProfit, A[j] - A[i])

    return maxProfit


print(solution([23171, 21011, 21123, 21366, 21013, 21367]))
