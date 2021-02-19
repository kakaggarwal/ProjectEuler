import sys

def houseBuyCount(a, n, b):
    count = 0

    for i in range(n):
        if a[i] <= b:
            b = b - a[i]
            count = count + 1
            

    return count


t = int(input().strip())

for i in range(t):
    n, b = input().strip().split(' ')
    n, b = [int(n), int(b)]

    a = [int(x) for x in input().split()]


    print(f'Case #{i+1}: {houseBuyCount(a, n, b)}')