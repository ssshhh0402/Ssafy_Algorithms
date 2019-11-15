from collections import deque
def find(a):
    stck = deque(a)
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[a[0][0]][a[0][1]] = 1
    time = 0
    while time != K:
        pos = []
        value = []
        for _ in range(len(stck)):
            i_x, i_y, c = stck.popleft()
            if not c:
                base[i_x][i_y] = 0
            else:
                c -= 1
                stck.append((i_x, i_y, c))
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = i_x + dx, i_y + dy
                if 0 <= x < M and 0 <= y < N and base[x][y]:
                    if not visited[x][y]:
                        pos.append((x, y))
                        value.append(base[x][y])
                        visited[x][y] = 1
                    else:
                        for i in range(len(pos)):
                            if pos[i] == (x, y):
                                if value[i] < base[x][y]:
                                    value[i] = base[x][y]

        for i in range(len(pos)):
            stck.append((pos[i][0], pos[i][1], value[i]))
        time += 1
    return len(stck)


for tc in range(1, int(input())+1):
    N, M, K = map(int,input().split())
    base = [list(map(int,input().split())) for _ in range(N)]
    sleepings = []
    for i in range(N):
        for j in range(M):
            if base[i][j]:
                sleepings.append((i, j, base[i][j]))
    numbers = find(sleepings)
    print(numbers)