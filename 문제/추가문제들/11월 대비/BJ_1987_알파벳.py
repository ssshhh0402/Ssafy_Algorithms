import sys
def find(a, b, c,d):
    global gg
    flag = False
    if c == 26:
        gg = 26
        return
    for i in range(4):
        x, y = a + dx[i], b + dy[i]
        if 0 <= x < R and 0 <= y < C:
            idx = ord(base[x][y]) - ord('A')
            if not visited[idx]:
                flag = True
                d[idx] = 1
                find(x,y,c+1,d)
                d[idx] = 0
    if not flag:
        gg = max(gg, c)


R, C = map(int, sys.stdin.readline().split())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = [0 for _ in range(26)]
base = [list(input()) for _ in range(R)]
visited[ord(base[0][0]) - ord('A')] = 1
gg = 0
flag_2 = False
for i in range(4):
    x, y = 0+dx[i], 0+dy[i]
    if 0 <= x < R and 0 <= y < C:
        a = ord(base[x][y]) - ord('A')
        if not visited[a]:
            flag_2 = True
            visited[a] = 1
            find(x,y,2,visited)
            visited[a] = 0

if flag_2 :
    print(gg)
else:
    print(1)

