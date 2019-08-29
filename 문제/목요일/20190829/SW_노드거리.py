def find(start):

    q = []
    D = [0] * (V+1)
    D[start] = 0
    visited = [0] * (V+1)
    visited[start] = 1
    q.append(start)
    while q:
        a = q.pop(0)
        for item in G[a]:
            if not visited[item]:
                visited[item] = 1
                q.append(item)
                D[item] = D[a] + 1
        if a == End:
            return D[a]
    return 0




for tc in range(int(input())):
    V, E = map(int,input().split())
    G = [[] for _ in range(V+1)]
    count = [[0 for _ in range(V)]for _ in range(V)]
    for _ in range(E):
        v, g = map(int, input().split())
        G[v].append(g)
        G[g].append(v)
    Start, End = map(int, input().split())
    print('#{0} {1}'.format(tc+1, find(Start)))