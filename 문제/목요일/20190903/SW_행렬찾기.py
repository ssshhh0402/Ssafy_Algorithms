def find(arr):
    global visited, list_s
    stck = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited[arr[0]][arr[1]] = 1
    stck.append((arr[0], arr[1]))
    #list_s.append((arr[0], arr[1]))
    while True:
        n = stck.pop(0)
        for i in range(4):
            x, y = n[0] + dx[i], n[1] + dy[i]
            if 0 <= x < N and 0 <= y < N:
                if not visited[x][y] and base[x][y] != 0 :
                    visited[x][y] = 1
                    stck.append((x, y))
        if not stck:
            a = abs(n[0]-arr[0])+1
            b = abs(n[1]-arr[1])+1
            nul_b = a * b
            list_s.append((a, b))
            list_n.append(nul_b)
            break


for tc in range(int(input())):
    base = []
    N = int(input())
    list_s = []
    list_n = []
    result = ''
    for _ in range(N):
        base.append(list(map(int, input().split())))
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if base[i][j] != 0 and not visited[i][j]:
                find((i, j))

    list_s.sort(key=lambda a : (a[0] * a[1], a[0]))
    print(''.join(list_s))