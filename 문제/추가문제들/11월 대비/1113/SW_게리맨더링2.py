

def getLeft(a,b):
    stck = []
    while True:
        a += 1
        b -= 1
        if 0 <= a < N and 0 <= b < N:
            stck.append((a,b))
        else:
            break
    return stck


def getRight(a,b):
    stck = []
    while True:
        a += 1
        b += 1
        if 0 <= a < N and 0 <= b < N:
            stck.append((a,b))
        else:
            break
    return stck


N = int(input())
base = [list(map(int,input().split())) for _ in range(N)]
for i in range(N-2):
    for j in range(1, N-1):
        left = getLeft(i,j)
        right = getRight(i,j)
