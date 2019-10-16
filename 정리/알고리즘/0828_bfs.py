V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
D = [0] * (V + 1)           #최단 거리 저장하기 위한 list
P = [0] * (V + 1)            #최단 경로 트리 저장하는 list


def BFS(s):
    visited = [0] * (V+1)  #여기서 n 은 입력받는 개수
    qu = []
    qu.append(s)
    visited[s] = 1
    D[s],P[s] = 0, 1
    while qu:
        a = qu.pop(0)
        print(a)
        # if not visited[a]:                                    #두가지 방법 모두 가능
        #     visited[a] = 1
        # for idx in G[a]:
        #     qu.append(idx)
        for w in G[a]:
            if not visited[w]:
                visited[w] = 1
                qu.append(w)
                D[w] = D[v] + 1
                P[w] = v





for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
BFS(1)