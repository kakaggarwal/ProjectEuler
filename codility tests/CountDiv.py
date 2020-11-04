def solution(A):
    upperDivCount = math.floor(B / K)
    lowerDivCount = math.floor((A - 1) / K)

    return upperDivCount - lowerDivCount
