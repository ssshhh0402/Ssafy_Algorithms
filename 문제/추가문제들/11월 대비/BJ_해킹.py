from collections import deque

def find(a):
    global result_num, result
    count = 0
    stck = deque(G[a])
    visited = [0 for _ in range(N+1)]
    while stck:
        for _ in range(len(stck)):
            x = stck.popleft()
            visited[x] = 1
            for item in G[x]:
                if not visited[item]:
                    stck.append(item)
        count += 1
    if count > result_num:
        result_num = count
        result.append([a])
    elif count == result_num:
        result[-1].append(a)


N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
result = []
result_num = 0
for _ in range(M):
    g, v = map(int, input().split())
    G[v].append(g)
for i in range(1, N+1):
    if G[i]:
        find(i)

print(* sorted(result[-1]))