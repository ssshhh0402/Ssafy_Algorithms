def change(a,b,c):
    global base
    base[a][b] = c
    dir = [(-1,0), (1,0),(0,-1),(0,1),(1,1),(-1,-1),(-1,1),(1,-1)]
    k = 0

    while k != len(dir):                                                                #상하좌우 대각선 쭉 확인하기
        stck = []                                                                         # 다른 색 => stck에 넣기
        x = a                                                                               # 같은 색 => stck에 있는 애들 색깔 변경
                                                                                                # 없는 곳이면 끝?
                                                                                        # 범위 나가면 => 끝
        y = b
        while True:
            x, y = x + dir[k][0], y + dir[k][1]
            if not 0 <= x < N or not 0 <= y < N or base[x][y] == 0:
                break
            elif base[x][y] == c:
                while stck:
                    n = stck.pop(0)
                    base[n[0]][n[1]] = c
                break
            else:
                stck.append((x, y))
        k += 1




for tc in range(int(input())):
    c_o = 0
    c_t = 0
    N, M = map(int, input().split())
    base = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for y in range((N//2)-1, (N//2) + 1, 1):
        for x in range((N//2)-1, (N//2)+1, 1):
                if (x+y) % 2 == 0:
                    base[x][y] = 2
                else:
                    base[x][y] = 1
    for _ in range(M):
        a, b, c = map(int, input().split())
        change(b-1,a-1,c)
    for i in range(N):
        c_o += base[i].count(1)
        c_t += base[i].count(2)
    print('#{0} {1} {2}'.format(tc+1, c_o, c_t))