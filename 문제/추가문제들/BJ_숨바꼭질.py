import sys
from collections import deque
def find(start):
    global visited
    stck = deque()
    result = []
    D = [0 for _ in range(1000001)]
    stck.append(start)

    while stck:
        n = stck.popleft()
        if n == K:
            result.append(D[n])
        else:
            if not visited[n]:
                visited[n] = 1
                if 0 <= n - 1:
                    if not D[n-1] or D[n-1] > D[n]+1:
                        stck.append(n-1)
                        D[n-1] = D[n] + 1
                if 0 <= n + 1 <= K+1:
                    if not D[n+1] or D[n+1] > D[n] + 1:
                        stck.append(n+1)
                        D[n+1] = D[n] + 1
                if 0 <= n + n <= K+1:
                    if not D[n+n] or D[n + n] > D[n] + 1:
                        stck.append(n + n)
                        D[n+n] = D[n] + 1

    return min(result)


N,K = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(1000001)]
a = find(N)
print(a)