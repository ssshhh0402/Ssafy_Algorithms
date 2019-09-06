# 각 카메라 별로
# 돌리는 방향 별
# 함수 호출?
# 그래서 모든 감시 카메라 확인 다했으면?
# 끝
import copy
def gam(a, b):                                              #카메라 보는길 반환
    dx = [1,-1]
    imsi = []
    if base[a][b] == 1:
        imsi_s = []
        for i in range(2):
            y = b + dx[i]
            while 0 <= y < M:
                if base[a][y] != 6 and not visited[a][y]:
                    imsi_s.append((a, y))
                elif base[a][y] == 6:
                    break
                y += dx[i]
            imsi.append(copy.deepcopy(imsi_s))
            imsi_s.clear()
        for i in range(2):
            x = a + dx[i]
            while 0 <= x < N:
                if base[x][b] != 6 and not visited[x][b]:
                    imsi_s.append((x,b))
                elif base[x][b] == 6:
                    break
                x += dx[i]
            imsi.append(copy.deepcopy(imsi_s))
            imsi_s.clear()
    elif base[a][b] == 2:
        imsi_s = []
        for i in range(2):
            y = b + dx[i]
            while 0 <= y < M:
                if base[a][y] != 6 and not visited[a][y]:
                    imsi_s.append((a,y))
                elif base[a][y] == 6:
                    break
                y += dx[i]
        imsi.append(imsi_s)
        imsi_s.clear()
        for i in range(2):
            x = b + dx[i]
            while 0 <= x < M:
                if base[x][b] != 6 and not visited[x][b]:
                    imsi_s.append((x,b))
                elif base[x][b] == 6:
                    break
                x += dx[i]
        imsi.append(imsi_s)
        imsi_s.clear()
    elif base[a][b] == 3:
        imsi_s = []

    return imsi


def find(arr_1, arr_2):         #arr_1 = 감시카메라 있는 아이 arr_2 = 색칠 되어 있는 아이
    if len(arr_1) == 0:
        print(arr_2)

    else:
        x,y = arr_1.pop()
        a = gam(x, y)
        while a:
            n = a.pop()
            imsi = copy.deepcopy(arr_2)
            for item in n:
                imsi[item[0]][item[1]] = 1
            find(arr_1, imsi)
            # find(arr_1, imsi)



N,M = map(int,input().split())
base= [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
list_c = []
for i in range(N):
    for j in range(M):
        if base[i][j] != 0 and base[i][j] != 6:
           list_c.append((i,j))
find(list_c, visited)
