import sys

#이거 불이랑 똑같이 짜면 안되냐
def air(x, y, q):
    a, b = x, y
    imsi = 0
    if not q:
        while b != C-1:
            if base[a][b] == -1:
                b += 1
                continue
            elif base[a][b] != 0:
                imsi, base[a][b] = base[a][b], imsi
            else:
                base[a][b] = imsi
                imsi = 0
            b += 1
        while a != 0:
            if base[a][b] == -1:
                a -= 1
                continue
            elif base[a][b] != 0:
                imsi, base[a][b] = base[a][b], imsi
            else:
                base[a][b] = imsi
                imsi = 0
            a -= 1
        while b != 0:
            if base[a][b] == -1:
                b -= 1
                continue
            elif base[a][b] != 0:
                imsi, base[a][b] = base[a][b], imsi
            else:
                base[a][b] = imsi
                imsi = 0
            b -= 1
        while a != x:
            if base[a][b] == -1:
                a += 1
                continue
            elif base[a][b] != 0:
                imsi, base[a][b] = base[a][b], imsi
            else:
                base[a][b] = imsi
                imsi = 0
            a += 1
    else:
        while b != C-1:
            if base[a][b] == -1:
                b += 1
                continue
            elif base[a][b] != 0:
                imsi, base[a][b] = base[a][b], imsi
            else:
                base[a][b]= imsi
                imsi = 0
            b += 1
        while a != R-1:
            if base[a][b] == -1:
                a += 1
                continue
            elif base[a][b] != 0:
                imsi, base[a][b] = base[a][b], imsi
            else:
                base[a][b] = imsi
                imsi = 0
            a += 1
        while b != 0:
            if base[a][b] == -1:
                b -= 1
                continue
            elif base[a][b] != 0:
                imsi, base[a][b]= base[a][b], imsi
            else:
                base[a][b] = imsi
                imsi = 0
            b -= 1
        while a != x:
            if base[a][b] == -1:
                a -= 1
                continue
            elif base[a][b] != 0:
                imsi, base[a][b] = base[a][b], imsi
            else:
                base[a][b] = imsi
                imsi = 0
            a -= 1






R,C,T = map(int,sys.stdin.readline().split())
base = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
copied = [[0 for _ in range(C)] for _ in range(R)]
list_m = []
list_a = []
visited = []
dx = [0,-1,0,1]
dy = [1,0,-1,0]
count = 0
cnt = 0
for i in range(R):
    for j in range(C):
        if base[i][j] != 0 and base[i][j] != -1:
            list_m.append((i,j))
        elif base[i][j] == -1:
            list_a.append((i,j))

for _ in range(T):
    # 공기 움직이고
    for _ in range(len(list_m)):                                                                                                                    #
        a_x,a_y = list_m.pop()
        for i in range(4):
            x,y = a_x + dx[i], a_y + dy[i]
            if 0 <= x < R and 0 <= y < C and base[x][y] != -1:
                if ((x,y, base[a_x][a_y]//5)) not in visited:
                    visited.append((x, y, base[a_x][a_y]//5))
                list_m.append((x,y))
                cnt += 1
        base[a_x][a_y] = base[a_x][a_y] - (base[a_x][a_y] // 5) * cnt

        cnt = 0
    while visited:
        n_x,n_y,n_v = visited.pop()
        base[n_x][n_y] += n_v
   # 공기청정기 움직이고
    mode = 0
    for item in list_a:
        air(item[0],item[1],mode)
        mode += 1

sum_n = 0
for i in range(R):
    for j in range(C):
        if base[i][j] != -1:
            sum_n += base[i][j]
print(sum_n)