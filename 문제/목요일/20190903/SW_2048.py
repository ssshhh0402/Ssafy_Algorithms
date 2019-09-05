def change(a,b,c):
    global base, visited, dx, dy
    stck = []
    x = a
    y = b
    stck.append((a,b))
    while True:
        x,y = x+dx[c], y+dy[c]
        if not 0 <= x < int(N) or not 0 <= y < int(N) or base[a][b] == 0:
            break
        elif base[x][y] == 0:
            if c == 2 or c == 3:
                if x == 0 or x == int(N) - 1:
                    while 0 <= y <= int(N)-1:
                        if base[x][y] == base[x-dx[c]][y-dy[c]] and not visited[x][y]:
                            base[x][y] += base[x-dx[c]][y-dy[c]]
                            base[x-dx[c]][y-dy[c]] = 0
                            visited[x][y] = 1
                            break
                        elif base[x][y] != 0:
                            break
                        else:
                            imsi = base[x - dx[c]][y - dy[c]]
                            base[x - dx[c]][y - dy[c]] = 0
                            base[x][y] = imsi
                            x, y = x+dx[c], y+dy[c]
                elif y == 0 or y == int(N) - 1:
                    n = stck.pop(0)
                    base[x][y] = base[n[0]][n[1]]
                    base[n[0]][n[1]] = 0
                # imsi = base[a][b]
                # base[a][b] = 0
                # base[x][y] = imsi
                else:
                    stck.append((x, y))
            elif c == 0 or c == 1:
                if y == 0 or y == int(N) -1:
                    while 0 <= x <= int(N)-1 :
                        if base[x][y] == base[x - dx[c]][y - dy[c]] and not visited[x][y]:
                            base[x][y] += base[x - dx[c]][y - dy[c]]
                            base[x - dx[c]][y - dy[c]] = 0
                            visited[x][y] = 1
                            break
                        elif base[x][y] !=0:
                            break
                        else:
                            imsi = base[x - dx[c]][y - dy[c]]
                            base[x - dx[c]][y - dy[c]] = 0
                            base[x][y] = imsi
                            x, y = x+dx[c], y+dy[c]
                elif x == 0 or x == int(N) - 1:
                    n = stck.pop(0)
                    base[x][y] = base[n[0]][n[1]]
                    base[n[0]][n[1]] = 0
                else:
                    stck.append((x,y))
        elif base[x][y] == base[a][b] and not visited[x][y]:
            base[x][y] += base[a][b]
            base[a][b] = 0
            visited[x][y] = 1
            break
        else:
            n = stck.pop()
            imsi = base[a][b]
            base[a][b] = 0
            base[n[0]][n[1]] = imsi
            break


for tc in range(int(input())):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    N, S = list(input().split())
    visited = [[0 for _ in range(int(N))] for _ in range(int(N))]
    base = []

    for _ in range(int(N)):
        base.append(list(map(int, input().split())))
    if S == 'up':
        S = 0
    elif S == 'down':
        S = 1
    elif S == 'right':
        S = 2
    elif S == 'left':
        S = 3
    if S == 0:
        for x in range(int(N)):
            for y in range(int(N)):
                change(x,y,S)
    elif S == 1:
        for x in range(int(N)-1, -1, -1):
            for y in range(int(N)):
                change(x,y,S)
    elif S == 2:
        for x in range(int(N)):
            for y in range(int(N)-1, -1, -1):
                change(x,y,S)
    elif S == 3:
        for x in range(int(N)):
            for y in range(int(N)):
                change(x,y,S)
    print('#{0}'.format(tc+1))
    for x in range(int(N)):
        for y in range(int(N)):
            print(base[x][y], end=" ")
        print("")

