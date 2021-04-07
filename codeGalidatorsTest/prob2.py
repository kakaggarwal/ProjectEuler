
primes = [2, 3]

def findPrime(mayBePrime):
    if mayBePrime in primes:
        return True
    else:
        for num in range(primes[-1] + 2, mayBePrime + 1, 2):
            for divisor in primes:
                if divisor >= (num // 2):
                    primes.append(num)
                    break
                elif num % divisor == 0:
                    break

        return mayBePrime in primes

def findMaxPrimeDiff(l, r):
    if l > r:
        return - 1
    elif l == r:
        if findPrime(l):
            return 0
        else:
            return - 1
    else:
        firstPrime = -1

        for num in range(l, r + 1):
            if findPrime(num):
                firstPrime = num
                break
        
        secondPrime = -1

        for num in range(l + 1, r + 1)[::-1]:
            if findPrime(num):
                secondPrime = num
                break
        
        if firstPrime == -1:
            return - 1
        elif secondPrime == -1:
            return 0
        else:
            return secondPrime - firstPrime


def main():
    t = int(input().strip())

    for a0 in range(t):
        l, r = input().strip().split(' ')
        l, r = [int(l), int(r)]
        print(findMaxPrimeDiff(l, r))

main()
