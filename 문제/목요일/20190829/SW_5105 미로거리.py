def BFS(a, b):
    visit = [[0 for _ in range(N)] for _ in range(N)]
    xi = [0, -1, 0, 1]
    yi = [-1, 0, 1, 0]
    q = []
    D = [[-1 for _ in range(N)] for _ in range(N)]
    visit[a][b] = 1
    q.append((a,b))
    while q:
        v = q.pop(0)
        if base[v[0]][v[1]] == 3:
            return D[v[0]][v[1]]
        else:
            for k in range(4):
                x, y = v[0] + xi[k], v[1] + yi[k]
                if -1 < x < N and -1 < y < N and (x, y) != (a, b) and base[x][y] != 1 and not visit[x][y]:
                    visit[x][y] = 1
                    q.append((x, y))
                    D[x][y] = D[v[0]][v[1]] + 1
    return 0


for tc in range(int(input())):
    N = int(input())
    base = [list(map(int, list(input()))) for _ in range(N)]
    start = 0
    end = 0

    for j in range(N):
        for i in range(N):
            if base[j][i] == 2:
                start = j
                end = i

    print("#{0} {1}".format(tc+1, BFS(start, end)))
