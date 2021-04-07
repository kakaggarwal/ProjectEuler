import sys

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())

    sum = 0
    prevIndex = 0

    for a1 in range(n):
        row = [int(n_temp) for n_temp in input().strip().split(' ')]

        if a1 == 0:
            sum += row[0]
        else:
            print('prevIndex: ' + str(prevIndex))
            val = max(row[prevIndex], row[prevIndex + 1])
            prevIndex = row.index(val)
            print('val: ' + str(val) + 'prevIndex: ' + str(prevIndex))
            sum += val

    print(sum)
