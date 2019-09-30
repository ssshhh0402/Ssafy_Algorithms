def find(a, b):         #a = ㄴㄴ x열 좌표 b = 돈
    global money
    if a == N:
        money = min(money, b)
        return
    if b >= money:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find(a+1, b+base[a][i])
            visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    base = [list(map(int,input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    money = 0xffffff
    for i in range(N):
        visited[i] = 1
        find(1,base[0][i])
        visited[i] = 0

    print("#{0} {1}".format(tc, money))