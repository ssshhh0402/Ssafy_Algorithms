import sys
from collections import deque
# sys.stdin = open('불 input.txt', 'r')
def find(person):
    global list_f, stck_p
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    D = [[0 for _ in range(w)] for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    stck_p.append((person[0],person[1]))

    tal = False
    result = 0
    while stck_p:
        for _ in range(len(list_f)):
            fire = list_f.popleft()
            for i in range(4):
                a,b = fire[0]+dx[i] , fire[1]+dy[i]
                if 0 <= a < h and 0 <= b < w and not fired[a][b] and base[a][b] != '#':
                    base[a][b] = '*'
                    list_f.append((a,b))
                    fired[a][b] = 1
        for _ in range(len(stck_p)):
            p = stck_p.popleft()
            if p[0] == 0 or p[1] == 0 or p[0] == h - 1 or p[1] == w - 1:
                if result == 0:
                    result = D[p[0]][p[1]] + 1
                else:
                    result = min(result, D[p[0]][p[1]]+1)
                tal = True
            else:
                for i in range(4):
                    x, y = p[0] + dx[i], p[1] + dy[i]
                    if 0 <= x < h and 0 <= y < w and base[x][y] == '.' and not visited[x][y]:
                        stck_p.append((x,y))
                        D[x][y] = D[p[0]][p[1]] + 1
                        visited[x][y] = 1
    return (tal, result)


for tc in range(int(sys.stdin.readline())):
    w , h = map(int, sys.stdin.readline().split())
    base = [list(sys.stdin.readline())[:-1] for _ in range(h)]
    fired=[[0 for _ in range(w)] for _ in range(h)]
    list_f = deque()
    stck_p = deque()
    s_x = 0
    s_y = 0
    f_x = 0
    f_y = 0
    for x in range(h):
        for y in range(w):
            if base[x][y] == '@':
                s_x = x
                s_y = y
                continue
            elif base[x][y] == '*':
                list_f.append((x,y))
    a = find((s_x, s_y))
    if a[0] :
        print(a[1])
    else:
        print('IMPOSSIBLE')
