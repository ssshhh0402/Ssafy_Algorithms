V, E = map(int,input().split())
G = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v,w))
    G[v].append((u, w))

pi = [0] * V
key = [0xffffff] * V
visited = [False] * V
key[0] = 0
cnt = V
while cnt:          #모든 정점을 다 선택 할 때 까지
                    #Tree에 연결되어 있지 않고, key 값이 최소인 정점음ㄹ 찾는다.
    u, min_n = 0, 0xffffff
    for i in range(V):
        if min_n > key[i] and not visited[i]:
            u, min_n = i, key[i]
    visited[u] = True

    for v, w in G[u]:
        if not visited[v] and w < key[v]:
            key[v] = w
            pi[v] = u

    cnt -= 1

print(*pi)