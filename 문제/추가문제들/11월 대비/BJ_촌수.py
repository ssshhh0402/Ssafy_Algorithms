from collections import deque


def find(a):
    stck = deque()
    count = 0
    visit = [0 for _ in range(N+1)]
    for i in G[a]:
        stck.append(i)
    while True:
        count += 1
        for _ in range(len(stck)):
            n = stck.popleft()
            visit[n] = 1
            if n == b:
                return count
            else:
                for i in G[n]:
                    if not visit[i]:
                        stck.append(i)
        if not stck:
            break
    return -1


N = int(input())
a, b = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(int(input())):
    g, v = map(int, input().split())
    G[g].append(v)
    G[v].append(g)
print(find(a))
