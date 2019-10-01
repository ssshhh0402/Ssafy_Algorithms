from collections import deque
def find(a):
    global comp, max_num
    stck = deque(G[a])
    count = 1
    visited = [0 for _ in range(N+1)]
    while stck:
        for _ in range(len(stck)):
            n = stck.popleft()
            visited[n] = 1
            for i in G[n]:
                if not visited[i]:
                        stck.append(i)
        if stck:
            count += 1
    if count > max_num:
        comp.clear()
        comp.append(a)
        max_num = count
    elif count == max_num:
        comp.append(a)


N,M = map(int,input().split())
G = [[] for _ in range(N+1)]
comp = []
max_num = 0
for _ in range(M):
    g,v = map(int,input().split())
    G[v].append(g)
for idx in range(len(G)):
    if G[idx]:
        find(idx)
print(*sorted(comp))