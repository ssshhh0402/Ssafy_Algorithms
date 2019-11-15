from collections import deque


def find(a):    # a = 독위치 들어있는 리스트
    global time, blank
    stck = deque(a)
    used = [[0 for _ in range(N)] for _ in range(N)]
    for item in a:
        used[item[0]][item[1]] = 1
    i_time = 0
    i_blank = 0
    while stck:
        for _ in range(len(stck)):
            i_x, i_y = stck.popleft()
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = i_x + dx, i_y + dy
                if 0 <= x < N and 0 <= y < N and not used[x][y] and base[x][y] != 1:
                    if base[x][y] == 0:
                        i_blank += 1
                        used[x][y] = 1
                        stck.append((x, y))
                    elif base[x][y] == 2:
                        used[x][y] = 1
                        stck.append((x, y))
        i_time += 1
        if i_time > time:
            return
        if b_count == i_blank:
            if blank:
                time = min(time, i_time)
            else:
                blank = True
                time = min(time, i_time)
            return


def back(a):  # a = 선택한 아이들
    if len(a) == M:
        find(a)
        return
    for i in range(n):
        if not visit[i]:
            a.append(pos[i])
            visit[i] = 1
            back(a)
            visit[i] = 0
            a.pop()


N, M = map(int, input().split())
base = [list(map(int, input().split())) for _ in range(N)]
pos = []
blank = False
time = 0xffffff
b_count = 0
for i in range(N):
    for j in range(N):
        if base[i][j] == 2:
            pos.append((i,j))
        elif base[i][j] == 0:
            b_count += 1

select = []
n = len(pos)
visit = [0 for _ in range(n)]
for idx in range(n):
    select.append(pos[idx])
    visit[idx] = 1
    back(select)
    select.pop()
    visit[idx] = 0
if not blank:
    print(-1)
else:
    print(time)