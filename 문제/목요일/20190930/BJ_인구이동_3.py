def find():
    global count
    G = [[] for _ in range(N)]
    sum = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    while True:
        flag = False
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    for q in range(4):
                        x, y = i+dx[i], j + dy[i]
                        if 0 <= x < N and 0 <= y < N:
                            if L <= abs(base[i][j] - base[x][y]) <= R:
                                if j not in G[i]:
                                    G[i].append(j)
                                    flag = True

        print(G)

dx = [0,1,0,-1]
dy = [1,0,-1,0]
N,L,R = map(int, input().split())
base = [list(map(int,input().split())) for _ in range(N)]
count = 0
find()