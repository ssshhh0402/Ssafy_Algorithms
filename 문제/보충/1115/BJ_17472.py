from collections import deque
def island():
    global base, islands
    visited = [[0 for _ in range(M)]for _ in range(N)]
    count = 1
    for i in range(N):
        for j in range(M):
            if base[i][j] == 1 and not visited[i][j]:
                stck = deque([(i,j)])
                islands.append([(i,j)])
                base[i][j] = count
                visited[i][j] = 1
                while stck:
                    i_x, i_y = stck.popleft()
                    base[i_x][i_y] = count
                    for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                        x, y = i_x + dx, i_y + dy
                        if 0 <= x < N  and 0 <= y < M and not visited[x][y]:
                            if base[x][y] == 1:
                                visited[x][y] = 1
                                islands[-1].append((x,y))
                                stck.append((x,y))
                count += 1
    return count


def bridges():
    global bridge
    for idx in range(1, count):
        island = islands[idx]
        bridge_length = 0xffffff
        bridge_start = 0
        bridge_end = 0
        for spot in island:
            i_x, i_y = spot
            bridge_start = base[i_x][i_y]
             # 0 = 위, 1 = 아래, 2 = 왼, 3 = 오른
            for i in range(4):
                dist = 0
                dx , dy = dirc[i]
                x, y = i_x + dx, i_y + dy
                while 0 <= x < N and 0 <= y < M:
                    dist += 1
                    if base[x][y] != 0:
                        if base[x][y] != bridge_start:
                            if dist < bridge_length:
                                bridge_length = dist
                                bridge_end = base[x][y]
                                break
                            else:
                                break
                        else:
                            break
                    else:
                        x, y = x + dx, y + dy
        bridge.append((bridge_start,bridge_end,bridge_length))







N, M = map(int, input().split())
base = [list(map(int,input().split())) for _ in range(N)]
dirc = [(-1,0),(1,0),(0,-1),(0,1)]
islands = [[]]
count = island()
bridge = []
connected = [0 for _ in range(count)]
bridges()
print(bridge)
