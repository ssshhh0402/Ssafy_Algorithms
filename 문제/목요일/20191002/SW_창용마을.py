from collections import deque


def find(a):      #a = 스타트 위치, b = id값
    global visited
    visited[a] = 1
    stck = deque(G[a])
    while stck:
        n = stck.popleft()
        if not visited[n]:
            visited[n] = 1
            for i in G[n]:
                stck.append(i)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    visited = [0 for _ in range(N+1)]
    G = [[] for _ in range(N+1)]
    id = 0
    for _ in range(M):
        g,v = map(int, input().split())
        G[g].append(v)
        G[v].append(g)
    for i in range(N+1):
        if G[i] and not visited[i]:
            id += 1
            find(i)
            print(visited)
    print("#{0} {1}".format(tc,id + visited.count(0)-1))