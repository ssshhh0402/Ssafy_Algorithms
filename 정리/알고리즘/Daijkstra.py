from collections import deque

# def BFS(s):                         #전형적인 BFS
#     D = [0xffffff] * (V+1)          #D[] 초기값 설정
#     Q = deque()
#     Q.append(s)
#     D[s] = 0
#     while Q:
#         u = Q.popleft()
#         for v, w in G[u]:
#             if D[v] > D[u] + w:
#                 Q.append(v)
#                 D[v] += D[u] + 1

def BFS(s):
    D = [0xfffffff] * (V+1)
    visit = [False] * (V+1)
    D[s] = 0
    cnt = V
    while cnt:
        #아직 선택되지 않은 정점 중에 D값이 최소인 부분을 찾는다. = u
        #이거 구현 안된거지?
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
        cnt -= 1

V, E = map(int, input().split())
G = [[] for _ in range(V)]
for _ in range(E):
    u,v,w = map(int,input().split())
    G[u] = (v,w)
    G[v] = (u,w)