from copy import deepcopy


def find(a,b,c, d):
    global deserts
    lists = deepcopy(c)
    pos = True
    for point in d:
        if 0 <= point[0] < N and 0 <= point[1] < N:
            if base[point[0]][point[1]] not in lists:
                lists.append(base[point[0]][point[1]])
            else:
                pos = False
                break
        else:
            pos = False
            break
    if pos:
        points = [(a+2, b), (a+2, b+2), (a+3, b+1)]
        find(a+1, b+1, lists,points)
        points = [(a+2, b), (a+2, b-2), (a+3, b-1)]
        find(a+1, b-1, lists,points)
    else:
        if len(c) >= 4:
            deserts = max(deserts, len(c))
        return


for tc in range(1, int(input())+1):
    N = int(input())
    visited = [[0 for _ in range(N)]for _ in range(N)]
    base = [list(map(int,input().split())) for _ in range(N)]
    deserts = -1
    for i in range(N):
        for j in range(N):
            value = base[i][j]
            visited[i][j] = 1
            points = [(i+1, j+1), (i+1, j-1), (i+2, j)]
            find(i,j, [value],points)
            visited[i][j] = 0
    if deserts == -1:
        print(-1)
    else:
        print(deserts)