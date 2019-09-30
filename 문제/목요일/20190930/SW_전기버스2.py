def find(a,b,c):      #a = 위치, b = 에너지  c = 충전횟수
    global count
    if b < 0:
        return

    if a >= N or b >= N - a:
        count = min(c, count)
        return
    if c < count:
        if b == 0:
            if base[a] == 0:
                return
            else:
                find(a+1, base[a]-1, c+1)
        else:
            find(a+1, base[a]-1, c+1)                   #현재 정류장 교환
            find(a+1, b-1, c)                             #현재 정류장 교환 x


for tc in range(1, int(input())+1):
    base = list(map(int, input().split()))
    N = base[0]
    base = [0]+base[1:]
    count = 0xffffff
    find(2, base[1]-1, 0)
    print("#{0} {1}".format(tc, count))