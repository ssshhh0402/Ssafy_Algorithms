def BFS(a, b):
    visit = [[0 for _ in range(N)] for _ in range(N)]
    xi = [0, -1, 0, 1]
    yi = [-1, 0, 1, 0]
    q = []
    visit[a][b] = 1
    q.append((a,b))
    while q:
        a = q.pop()
        if base[a[0]][a[1]] == 3:
            return 1
        else:
            for k in range(4):
                x, y = a[0] + xi[k], a[1] + yi[k]
                if -1 < x < N and -1 < y < N and (x,y) != (a, b) and base[x][y] == 0 and not visit[x][y]:
                    visit[x][y] = 1
                    q.append((x, y))
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
