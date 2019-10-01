def find(a,b,c,d):          #x좌표 y좌표 c = 갯수 d = 문장
    global result
    if c == 7:
        result.add(d)
        return
    elif c > 7:
        return
    for i in range(4):
        x, y = a+dx[i], b+dy[i]
        if 0 <= x < 4 and 0 <= y < 4:
            find(x, y, c+1, d+base[x][y])


for tc in range(1, int(input())+1):
    base = [list(input().split()) for _ in range(4)]
    result = set()
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        for j in range(4):
            find(i,j,1,base[i][j])
    print("#{0} {1}".format(tc, len(result)))