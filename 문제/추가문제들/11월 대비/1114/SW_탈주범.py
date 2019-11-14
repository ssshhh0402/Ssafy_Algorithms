from collections import deque


def find(a, b):      # a : x, b : y
    stck = deque([(a,b)])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    time = 1
    while stck:
        for _ in range(len(stck)):
            i_x, i_y = stck.popleft()
            visited[i_x][i_y] = 1
            pipe = base[i_x][i_y]
            if not pipe:
                continue
            else:
                for dx, dy in pipes[pipe]:
                    x, y = i_x + dx, i_y + dy
                    if 0 <= x < N and 0 <= y < M and not visited[x][y]:
                        if base[x][y]:
                            next_pipe = base[x][y]
                            for next_x, next_y in pipes[next_pipe]:
                                if (x + next_x, y + next_y) == (i_x, i_y):
                                    stck.append((x, y))

        if time == L:
            break
        else:
            time += 1
    value = 0
    for visit in visited:
        value += sum(visit)
    return value

for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int,input().split())
    base = [list(map(int,input().split())) for _ in range(N)]
    pipes = [[], [(0, 1), (1, 0), (0, -1), (-1, 0)], [(1, 0), (-1, 0)], [(0, -1), (0, 1)], [(-1, 0), (0, 1)], [(0,1), (1,0)], [(0, -1), (1, 0)],[(0, -1), (-1, 0)]]
    time = find(R,C)
    print("#{0} {1}".format(tc, time))