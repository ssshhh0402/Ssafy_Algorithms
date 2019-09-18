N = int(input())
base = [list(map(int, input().split())) for _ in range(N)]
dx = [0,1,1]
dy = [1,1,0]
cnt = 0

def find(a, b):
    global cnt
    if a == ((N-1,N-1)):
        cnt += 1
    else:
        x, y = a[0], a[1]
        if b == 0:
            if 0 <= x < N and 0 <= y+1 < N and not base[x][y+1] :
                find((x,y+1), 0)
            if 0 <= x+1 < N and 0 <= y+1 < N and not base[x+1][y+1] and not base[x+1][y] and not base[x][y+1]:
                find((x+1,y+1), 1)
        elif b == 1:
            if 0 <= x < N and 0 <= y+1 < N and not base[x][y+1] :
                find((x,y+1), 0)
            if 0 <= x+1 < N and 0 <= y+1 < N and not base[x+1][y+1] and not base[x+1][y] and not base[x][y+1]:
                find((x+1,y+1), 1)
            if 0 <= x+1 < N and 0 <= y  < N and not base[x+1][y] :
                find((x+1,y), 2)
        else:
            if 0 <= x+1 < N and 0 <= y+1 < N and not base[x+1][y+1] and not base[x+1][y] and not base[x][y+1]:
                find((x+1,y+1), 1)
            if 0 <= x+1 < N and 0 <= y < N and not base[x+1][y] :
                find((x+1, y), 2)


find((0,1), 0)
print(cnt)