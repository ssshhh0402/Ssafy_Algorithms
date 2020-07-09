from collections import deque

N, M, T = map(int, input().split())
base = [deque(map(int, input().split())) for _ in range(N)]
used = [deque([1 for _ in range(M)] for _ in range(N))]

for _ in range(T):
    find = False
    x, d, k = map(int, input().split())
    change = []
    for X in range(x-1, N, x):
        if not d:
            base[X].rotate(k)
            used[X].rotate(k)
        else:
            base[X].rotate(-k)
            used[X].rotate(-k)
    for x in range(N):
        for y in range(M):
            imsi_v = base[x][y]
            if imsi_v:
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    a, b = x+dx, y + dy
                    if 0 <= a < N:
                        if b == M:
                            b = b - M
                        if base[a][b] == imsi_v:
                            change.append((a, b))
                            change.append((x, y))
            else:
                used[x][y] = 0
    if not change:
        avg_sum = 0
        avg_count = 0
        for Y in range(N):
            avg_sum += sum(base[Y])
            avg_count += sum(used[Y])
        avg_array = avg_sum / avg_count
        for i_x in range(N):
            for i_y in range(M):
                if base[i_x][i_y]:
                    if base[i_x][i_y] > avg_array:
                        base[i_x][i_y] -= 1
                    elif base[i_x][i_y] < avg_array:
                        base[i_x][i_y] += 1
    else:
        for x, y in change:
            base[x][y] = 0
            used[x][y] = 0

count = 0
for index in range(N):
    count += sum(base[index])

print(count)


