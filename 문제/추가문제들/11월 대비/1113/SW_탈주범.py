from collections import deque


def find(a, b):      # a : x, b : y
    stck = deque([(a, b)])
    # visited = [[0 for _ in range(M)] for _ in range(N)]
    # visited[a][b] = 1
    time = 1
    while stck:
        for _ in range(len(stck)):
            i_x, i_y = stck.popleft()
            pipe = base[i_x][i_y]
            if not pipe:
                continue
            else:
                for item in pipes[pipe]:
                    dx, dy = item
                    x, y = i_x + dx, i_y + dy
                    if 0 <= x < N and 0 <= y < M:
                        if base[x][y]:
                            if (x, y) not in stck:
                                stck.append((x, y))
        time += 1
        if time == L:
            return len(stck)


for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int,input().split())
    base = [list(map(int,input().split())) for _ in range(N)]
    pipes = [[], [(0, 1), (1, 0), (0, -1), (-1, 0)], [(1, 0), (-1, 0)], [(0, -1), (0, 1)], [(-1, 0), (0, 1)], [(0,1), (1,0)], [(0, -1), (1, 0)],[(0, -1), (-1, 0)]]

    time = find(C,R)
    print("#{0} {1}".format(tc, time))