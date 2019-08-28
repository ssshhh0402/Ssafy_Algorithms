def path(x,y,max):
    if x == max or y == max or y < 0 or x < 0:
        return 0
    elif not visit[x][y] and base[x][y] != 1:                                                       #위, 왼, 오른, 아래 이 순서대로
        visit[x][y] = 1
        if base[x][y] == 3 or path(x-1, y, max)or path(x, y-1, max) or path(x, y+1, max) or path(x+1, y, max):
            return 1
        else:
            return 0
    else:
        return 0


for tc in range(int(input())):
    N = int(input())
    find = False
    base = []
    start = 0
    end = 0
    visit = []
    for _ in range(N):
        imsi = []
        for _ in range(N):
            imsi.append(0)
        visit.append(imsi)
    for _ in range(N):
        base.append(list(map(int, list(input()))))

    for j in range(N):
        for i in range(N):
            if base[j][i] == 2:
                start = j
                end = i
                find = True
                break

    if find:
        print("#{0} {1}".format(tc+1, path(start, end, N)))
    else:
        print("#{0} {1}".format(tc + 1, 0))




  # elif x == 0:
    #     return 0
    # elif y == 0:
    #     if base[x-1][y] != 1 and not visit[x-1][y]:
    #         return path(x-1,y,max)
    #     elif base[x][y+1] == 1 and not visit[x][y+1]:
    #         return path(x, y+1, max)
    # elif y == max - 1:
    #     if base[x - 1][y] != 1 and not visit[x-1][y]:
    #         return path(x-1, y, max)
    #     elif base[x][y - 1] != 1 and not visit[x][y-1]:
    #         return path(x, y-1, max)
    # elif x == max - 1:
    #     if base[x - 1][y] != 1 and not visit[x-1][y]:
    #         return path(x-1, y, max)
    #     elif base[x][y - 1] != 1 and not visit[x][y-1]:
    #         return path(x, y-1, max)
    #     elif base[x][y + 1] != 1 and not visit[x][y+1]:
    #         return path(x, y+1, max)
    # else:
    #     if base[x - 1][y] != 1 and not visit[x-1][y]:
    #         return path(x-1, y, max)
    #     elif base[x][y-1] != 1 and not visit[x][y-1]:
    #         return path(x, y-1, max)
    #     elif base[x][y+1] != 1 and not visit[x][y+1]:
    #         return path(x, y-1, max)
