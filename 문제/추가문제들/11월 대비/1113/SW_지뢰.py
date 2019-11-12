from collections import deque


def find(a, b, c, d, e):            # a : 누르는 x, b : 누르는 y, c : 판 현재 상황, d = 누른 횟수, e = 남은 칸 갯수
    global result
    if not e:
        result = min(d, result)
        return
    if d > result:
        return
    stck = deque([(a, b)])
    c_list = []
    i_count = 0
    while stck:
        i_count += 1
        i_x, i_y = stck.popleft()
        count = 0
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            x, y = i_x+dx, i_y + dy
            if 0 <= x < N and 0 <= y < N and c[x][y]:
                if c[x][y] == '*':
                    count += 1
                elif c[x][y] == '.':
                    c_list.append((x,y))
        if count:
            c[i_x][i_y] = count
        else:
            c[i_x][i_y] = 0
            stck.extend(c_list)
    answer = e-i_count
    if not answer :
        result = min(result, d)
        return
    else:
        for save in safes:
            if c[save[0]][save[1]] == '.':
                find(save[0],save[1],c,d+1, answer)




for tc in range(1, int(input())+1):
    N = int(input())
    base = [list(input()) for _ in range(N)]
    safes = []
    result = 0xffffff
    for i in range(N):
        for j in range(N):
            if base[i][j] == '.':
                safes.append((i,j))
    e = len(safes)
    for save in safes:
        find(save[0],save[1],base, 1, e)
    print(result)