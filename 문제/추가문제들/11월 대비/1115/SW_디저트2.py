from copy import deepcopy


def find(a, b, c, d, e):            # a = x, b = y, c = 여태까지 지나온 값 d =  다음 확인할 아이들, e = 모드 c는 전역변수로 하는거 생각해보기
    global deserts
    pos = True
    lists = deepcopy(c)                             # 그럼 차라리 k번째 일때, 기준점을 a - k, b - k로 한다면..?맨위를 기준으로 한다면?
    for (x, y) in d:
        if 0 <= x < N and 0 <= y < N:
            if base[x][y] not in lists:
                lists.append(base[x][y])
            else:
                pos = False
                break
        else:
            pos = False
            break
    if not pos:
        if len(lists) >= 4 and not len(lists) % 2 :
            deserts = max(deserts, len(c))
    else:
        if not e:
            nexts = [(a+2, b-2), (a+3, b-1)]
            find(a+1, b-1, lists, nexts, 1)
            nexts = [(a+3, b+1), (a+2, b+2)]
            find(a+1, b+1, lists, nexts, 2)
        elif e == 1:
            nexts = [(a+2, b-2), (a+3, b-1)]
            find(a+1, b-1, lists, nexts, e)
        elif e == 2:
            nexts = [(a+3, b+1), (a+2, b+2)]
            find(a+1, b+1, lists, nexts, e)


for tc in range(1, int(input())+1):
    N = int(input())
    base = [list(map(int, input().split())) for _ in range(N)]
    deserts = -1
    for i in range(N):
        for j in range(N):
            value = base[i][j]
            points = [(i+1, j-1), (i+1, j+1), (i+2, j)]
            find(i, j, [value], points, 0)
    if deserts == -1:
        print("#{0} {1}".format(tc, -1))
    else:
        print("#{0} {1}".format(tc, deserts))