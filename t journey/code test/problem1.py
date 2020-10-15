class Point:
    def __init__(self, tag, dist):
        self.tag = tag
        self.dist = dist


def solution(S, X, Y):
    dists = [0] * len(S)

    for i in range(len(S)):
        dists[i] = (X[i] ** 2 + Y[i] ** 2) ** 0.5

    maxRad = max(dists)
    print(dists)
    similar = False

    for i in range(len(X)):
        for j in range(i + 1, len(X)):
            if S[i] == S[j]:
                similar = True
                maxRad = max(dists[i], dists[j])

    if maxRad == max(dists) and similar == False:
        return len(dists)

    count = 0

    for dist in dists:
        if dist < maxRad:
            count += 1

    return count


print(solution('ABACD', [2, -1, -4, -3, 3], [2, -2, 4, 1, -3]))
