''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def isInfected(v, b):
    if len(b) > 0:
        lastIndex = v.find(b[0])

        if lastIndex == -1:
            return 'NEGATIVE'    

        for ch in b[1:]:
            index = v.find(ch, lastIndex)

            if index == -1:
                return 'NEGATIVE'
            else:
                lastIndex = index
        
        return 'POSITIVE'
    else:
        return 'NEGATIVE'

def main():
    v = input().strip()
    n = int(input().strip())

    for a0 in range(n):
        b = input().strip()
        
        print(isInfected(v, b))

main()

