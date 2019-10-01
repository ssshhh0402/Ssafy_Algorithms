from collections import deque


def find(a,b,c):      #a = x, b = y, c = 시작 방 ,d = 갯수
    global min_num, min_r
    stck = deque([(a, b)])
    count = 0
    while stck:
        count += 1
        for _ in range(len(stck)):
            a_2, b_2 = stck.popleft()
            for i in range(4):
                x, y = a_2 + dx[i], b_2 + dy[i]
                if 0 <= x < N and 0 <= y < N and base[x][y] - base[a_2][b_2] == 1:
                    stck.append((x, y))
    if count > min_r:
        min_r = count
        min_num = c
    elif count == min_r:
        if min_num > c:
            min_num = c


for tc in range(1, int(input())+1):
    N = int(input())
    base = [list(map(int, input().split())) for _ in range(N)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    min_r = 0
    min_num = 0xffff
    for i in range(N):
        for j in range(N):
            find(i, j, base[i][j])
    print("#{0} {1} {2}".format(tc, min_num, min_r))