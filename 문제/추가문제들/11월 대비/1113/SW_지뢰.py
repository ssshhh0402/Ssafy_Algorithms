from collections import deque


def find(a,b,c,d):            # a = x좌표, b = y좌표, c = 남은 . 갯수 d = 횟수
    global changed, result
    changed[a][b] = 1
    stck = deque([(a,b)])
    i_count = 0
    remember = []
    while stck:
        i_list = []
        i_count += 1
        i_x, i_y = stck.popleft()
        base[i_x][i_y] = 0
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:

            x, y = i_x + dx, i_y + dy
            if 0 <= x < N and 0 <= y < N:
                if not changed[x][y]:
                    i_list.append((x, y))
                else:
                    if base[x][y] == '*':
                        base[i_x][i_y] += 1
        if not base[i_x][i_y]:
            stck.extend(i_list)
            remember.extend(i_list)
    g = c - i_count
    if not g:
        result = min(result, d)
        return
    else:
        for item in remember:
            changed[item[0]][item[1]] = 1
        for x in range(N):
            for y in range(N):
                if not changed[x][y]:
                    find(x, y, g, d+1)
        for item in remember:
            changed[item[0]][item[1]] = 0
            base[item[0]][item[1]] = '.'
    base[a][b] = '.'
    changed[a][b] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    base = [list(input()) for _ in range(N)]
    changed = [[0 for _ in range(N)] for _ in range(N)]
    safes = 0
    result = 0xffffff
    for i in range(N):
        for j in range(N):
            if base[i][j] == '*':
                changed[i][j] = 1
            elif base[i][j] == '.':
                safes += 1
    for a in range(N):
        for b in range(N):
            if not changed[a][b]:
                find(a, b, safes, 1)
    print("#{0} {1}".format(tc, result))