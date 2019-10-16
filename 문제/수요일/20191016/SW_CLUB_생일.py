from collections import deque

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    D = [0 for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int,input().split())
        G[a].append(b)
        G[b].append(a)
    stck = deque([1])
    i = 0
    while i <= 2:
        for _ in range(len(stck)):
            n = stck.popleft()
            D[n] = 1
            for v in G[n]:
                if not D[v]:
                    stck.append(v)
        i += 1
    print("#{} {}".format(tc, sum(D)-1))