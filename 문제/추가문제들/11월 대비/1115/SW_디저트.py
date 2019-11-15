from copy import deepcopy


def find(a, b, c, d, e):
    global deserts
    lists = deepcopy(c)
    points = [(a+1, b-1), (a+1, b+1), (a+2, b)]
    pos = True
    for point in points:
        if 0 <= point[0] < N and 0 <= point[1] < N:
            if base[point[0]][point[1]] not in lists:
                lists.append(base[point[0]][point[1]])
            else:
                if point not in d:
                    pos = False
                    break
        else:
            pos = False
            break
    if pos:
        if not e:
            find(a+1, b+1, lists, points, 1)
            find(a+1, b-1, lists, points, 2)
        elif e == 1:
            find(a+1, b+1, lists, points, e)
        elif e == 2:
            find(a+1, b-1, lists, points, e)
    else:
        if len(c) >= 4:
            deserts = max(deserts, len(c))
        return


for tc in range(1, int(input())+1):
    N = int(input())
    base = [list(map(int, input().split())) for _ in range(N)]
    deserts = -1
    for i in range(N):
        for j in range(N):
            value = base[i][j]
            find(i, j, [value], [],0)
    if deserts == -1:
        print("#{0} {1}".format(tc, -1))
    else:
        print("#{0} {1}".format(tc, deserts))