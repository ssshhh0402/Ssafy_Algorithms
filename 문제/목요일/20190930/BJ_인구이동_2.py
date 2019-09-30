
def find(a):
    global count
    G = [[] for _ in range(N)]
    sum = 0
    while True:
        flag = False
        for i in range(N):
            for j in range(N):
                for q in range(4):
                    x,y = i + dx[q], j + dy[q]
                    if 0 <= x < N and 0 <= y < N:
                        if not visited[x][y] and L <= abs(base[i][j] - base[x][y]) <= R:
                            if j not in G[i]:
                                G[i].append(j)
                                sum += base[i][j]
                                flag = True
                            if y not in G[x]:
                                G[x].append(y)
                                sum += base[x][y]
                                flag = True
        if not flag:
            break
        else:
            sum = 0
            for idx in G:
                for a in idx:
                   sum += a
            for idx in G:
                for a in idx:

                base[i[0]][i[1]] = sum // len(imsi)
            visited = [[0 for _ in range(N)] for _ in range(N)]
            count += 1
            imsi.clear()
            sum = 0
        for i in range(len(base)):
            print(base[i])
        print('---------------------------------------')


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, L, R = map(int, input().split())
base = [list(map(int, input().split())) for _ in range(N)]
count = 0
find(0)
print(count)