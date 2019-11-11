from collections import deque


def target(a):       # 같은 거리에서 먹을수 있는 아이들
    n_target = (0, 0)
    if len(a) == 1:
        n_target = a[0]
    else:
        imsi = []
        imsi_x = 0xffffff
        for item in a:              # 가장 위에 있는 물고기 탐색
            if item[0] < imsi_x:
                imsi.clear()
                imsi.append(item)
                imsi_x = item[0]
            elif item[0] == imsi_x:
                imsi.append(item)
        if len(imsi) == 1:          # 가장 위에 있는 물고기가 여러마리일 경우
            n_target = imsi[0]
        else:
            imsi_y = 0xffffff
            for items in imsi:          # 가장 왼쪽에 있는 물고기 탐색
                if items[1] < imsi_y:
                    n_target = items
    return n_target


def find(a,b,c):            # a : 시작지점 x, b = 시작지점 y, c = 시간
    global shark, count, base
    visited = [[0 for _ in range(N)] for _ in range(N)]
    base[a][b] = 0
    visited[a][b] = 1
    stck = deque([(a,b)])
    result = []
    imsi_c = 0
    count -= 1                      #물고기를 먹었을 경우, count -1
    if not count:                      # - 1 한 후 count 가 0일 경우 상어 크기 + 1
        shark += 1
        count = shark
    while stck:                             # bfs로 상어보다 작은 물고기 만날때 까지 탐색
        for _ in range(len(stck)):
            imsi_x, imsi_y = stck.popleft()
            for i_x, i_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = imsi_x + i_x, imsi_y + i_y
                if 0 <= x < N and 0 <= y < N and base[x][y] <= shark and not visited[x][y]:
                    visited[x][y] = 1
                    if base[x][y] == 0:             # 현재 위치가 빈칸일 경우
                        stck.append((x,y))
                    elif base[x][y] == shark:       # 현재 위치가 물고기인데 크기가 상어랑 같은 경우
                        stck.append((x,y))
                    else:                           # 그 나머지(물고기이고, 크기가 상어보다 작음)
                        result.append((x,y))
        imsi_c += 1
        if result:                          #c + imsi_c 시간걸려 갈수있는 곳에 물고기가 한마리라도 있는 경우
            n_fish = target(result)
            c = find(n_fish[0], n_fish[1], c + imsi_c)
            break
                                            #없는 경우 while문 계속 진행
    return c


N = int(input())
base = [list(map(int,input().split())) for _ in range(N)]
shark = 2
count = 3
start_x = 0
start_y = 0
for i in range(N):
    for j in range(N):
        if base[i][j] == 9:
            start_x = i
            start_y = j

time = find(start_x, start_y, 0)

print(time)