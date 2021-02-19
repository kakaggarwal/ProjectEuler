def solution(S):
    if len(S) % 2 != 0:
        return 0

    brackets = []

    for bracket in S:
        if bracket == '(':
            brackets.append(bracket)
        else:
            if len(brackets) > 0:
                brackets.pop()
            else:
                return 0

    if len(brackets) > 0:
        return 0
    else:
        return 1


# print(solution('(()(())())'))
print(solution('(()(())()))))'))
print(solution('(((((())))'))
