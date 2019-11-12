def find(a,b,c,d):          # a = x좌표, b = y좌표, c = 값 d = 길이
    global visited, cut, road
    for i_x, i_y in ([(1, 0), (0, 1), (-1, 0), (0, -1)]):           # 함수 인자로 받은 값 상하좌우 확인
        x, y = a+i_x, b+i_y
        if 0 <= x < N and 0 <= y < N and not visited[x][y]:             # 범위 내 이고 방문 안한 곳
            if base[x][y] < c:                                          # 이동할 곳이 현재 곳보다 낮은 곳
                visited[x][y] = 1
                find(x,y,base[x][y], d+1)
                visited[x][y] = 0
            else:                                                         # 이동할 부분이 현재 위치보다 높은 곳
                if not cut:                                               # 자른 거 없을 때
                    pos = False
                    imsi = 0
                    for idx in range(1, K+1):                                # K 까지 뒤지면서
                        if base[x][y] - idx < c:                               # 깍은 위치가 현재 보다 낮은 때 탐색
                            imsi = base[x][y] - idx
                            pos = True
                            break
                    if pos:                                                    # 깍아서 갈 수 있을 때
                        cut = True
                        visited[x][y] = 1
                        find(x,y,imsi,d+1)
                        visited[x][y] = 0
                        cut = False
                    else:                                                       # 깍아서 갈 수 없을 때
                        road = max(road, d)
                else:                                                           # 자른 거 있을 때
                    road = max(road, d)

for tc in range(1, int(input())+1):
    N, K = map(int,input().split())
    base = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    bongs = []
    bong = -0xffffff
    road = -0xffffff
    cut = False
    for i in range(N):
        for j in range(N):
            if base[i][j] > bong:
                bong = base[i][j]
                bongs.clear()
                bongs.append((i,j))
            elif base[i][j] == bong:
                bongs.append((i,j))
    for item in bongs:
        visited[item[0]][item[1]] = 1
        find(item[0], item[1], base[item[0]][item[1]],1)
        visited[item[0]][item[1]] = 0
    print("#{0} {1}".format(tc, road))