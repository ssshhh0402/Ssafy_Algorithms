import sys;

def DFS(v): # v = 현재 방문하는 정점

    visit[v] = True

    for w in G[v]:
        if not visit[w]:
            DFS(w)
    V, E = map(int, input().split())
    G = [[] for _ in range(v+1)]
