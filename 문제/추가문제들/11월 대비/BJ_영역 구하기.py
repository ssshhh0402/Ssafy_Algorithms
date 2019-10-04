from collections import deque

def find(a,b):
    global result
    stck = deque([(a,b)])
    count = 0
    while stck:
        count += 1
        c, d = stck.popleft()
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            x, y = c+dx, d+dy
            if 0 <= x < M and 0 <= y < N:
                if not visited[x][y]:
                    visited[x][y] = 1
                    stck.append((x,y))
    result.append(count)


M,N,K = map(int,input().split())
visited = [[0 for _ in range(N)] for _ in range(M)]
id = 0
result = []
for _ in range(K):
    arr = list(map(int, input().split()))
    for x in range(M-arr[3], M-arr[1]):
        for y in range(arr[0], arr[2]):
            visited[x][y] = 1


for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            id += 1
            visited[i][j] = 1
            find(i,j)

print(id)
print(*sorted(result))