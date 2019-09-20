def find(a,b,c):        #a = x b = y c = 합 d = visited
    global result
    if a == N-1 and b == N-1:
        result = min(result, c)
    for i in range(2):
        x, y = a + dx[i], b + dy[i]
        if 0<=x < N and 0 <= y < N:
            if c + base[x][y] < result:
                find(x,y,c+base[x][y])



for tc in range(1, int(input())+1):
    dx = [1,0]
    dy = [0,1]
    result = 0xffffff
    N = int(input())
    base = [list(map(int, input().split())) for _ in range(N)]
    find(0,0,base[0][0])
    print("#{0} {1}".format(tc,result))