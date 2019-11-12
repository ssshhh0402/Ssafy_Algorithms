def find(a,b,c,d):            # a : 누르는 x, b : 누르는 y, c : 판 현재 상황, d = 누른 횟수
    pass


for tc in range(1, int(input())+1):
    N = int(input())
    base = [list(input()) for _ in range(N)]
    safes = []
    result = 0
    for i in range(N):
        for j in range(N):
            if base[i][j] == '.':
                safes.append((i,j))
    for save in safes:
        find(save[0],save[1],base, 1)