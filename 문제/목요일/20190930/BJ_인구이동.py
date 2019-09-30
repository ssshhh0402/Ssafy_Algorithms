



def find(a):
    global count
    visited = [[0 for _ in range(N)]for _ in range(N)]
    imsi = []
    sum = 0
    while True:
        for i in range(N):
            for j in range(N):
                visited[i][j] = 1

                for q in range(4):
                    x,y = i + dx[q], j + dy[q]
                    if 0 <= x < N and 0 <= y < N:
                        if not visited[x][y] and L <= abs(base[i][j] - base[x][y]) <= R:
                            if (i,j) not in imsi:
                                imsi.append((i,j))
                                sum += base[i][j]
                            if (x,y) not in imsi:
                                imsi.append((x,y))
                                sum += base[x][y]
                            #visited[x][y] = 1
        if len(imsi) == 0:
            break
        else:
            for i in imsi:
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