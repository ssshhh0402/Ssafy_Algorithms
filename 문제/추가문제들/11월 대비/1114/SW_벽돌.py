from collections import deque
from copy import deepcopy

def bfs(a,b):   # a, b: bfs 돌려야하는 좌표
    stck = deque([(a,b)])
    power = base[a][b]
    b_count = -1
    k = 0
    visited = [[0 for _ in range(W)] for _ in range(H)]
    visited[a][b] = 1
    while k != power and stck:
        for _ in range(len(stck)):
            b_count += 1
            i_x, i_y = stck.popleft()
            base[i_x][i_y] = 0
            for dx, dy in [(0, 1), (0, -1)]:                    # 가로 탐색
                x, y = i_x + dx, i_y + dy
                if 0 <= y < H and not visited[x][y] and base[x][y]:
                    if base[x][y] == 1:
                        visited[x][y] = 1
                        stck.append((x, y))
                    else:
                        b_count += bfs(x, y)
        k += 1
    k = 0
    stck.append((a,b))
    while k != power and stck:                                  # 세로 탐색
        for _ in range(len(stck)):
            b_count += 1
            i_x, i_y = stck.popleft()
            for dx, dy in [(1, 0), (-1, 0)]:
                x, y = i_x + dx, i_y + dy
                if 0 <= x < W and not visited[x][y] and base[x][y]:
                    if base[x][y] == 1:
                        visited[x][y] = 1
                        stck.append((x, y))
                    else:
                        b_count += bfs(x, y)
        k += 1
    return b_count


def f_game(a):
    for height in range(H-1, -1, -1):
        if base[a][height] != 0:
            return bfs((a,height))


def find(a):
    if len(a) == N:
        for pos in a:
            result = f_game(pos)
        return

    for i in range(W):
        if not sum(base[i]):
            a.append(i)
            find(a)
            a.pop()


for tc in range(1, int(input())+1):
    N, W, H = list(map(int,input().split()))
    base = [list(map(int,input().split())) for _ in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if base[i][j] >= 1:
                count += 1
    for i in range(W):
        find([i])