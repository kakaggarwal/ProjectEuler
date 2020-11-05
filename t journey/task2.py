# def getMineCount():


def minesweeper(M):
    newM = []
    newM.append(["O"] * (len(M[0]) + 2))

    for row in M:
        newM.append(["O"] + list(row) + ["O"])

    newM.append(newM[0])

    for i in range(1, len(newM) - 1):
        for j in range(1, len(newM[i]) - 1):
            if newM[i][j] == "O":
                newM[i][j] = str([
                    newM[i - 1][j - 1],
                    newM[i - 1][j],
                    newM[i - 1][j + 1],
                    newM[i][j - 1],
                    newM[i][j],
                    newM[i][j + 1],
                    newM[i + 1][j - 1],
                    newM[i + 1][j],
                    newM[i + 1][j + 1]
                ].count("X"))

    for row in newM[1: -1]:
        print(row[1:-1])


print(minesweeper(["XOO", "OOO", "XXO"]))


# XOO
# OOO
# XXO
