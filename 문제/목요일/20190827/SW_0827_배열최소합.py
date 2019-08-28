def wornl(a, b, c):
    global list_min
    if a == b:
        list_min = c
    else:
        for j in range(b):
            if list_i[j] == 0 and c + base[a][j] < list_min:
                list_i[j] = 1
                c += base[a][j]
                wornl(a+1, b, c)
                list_i[j] = 0
                c -= base[a][j]


for tc in range(int(input())):
    N = int(input())
    base = [list(map(int, input().split()))for _ in range(N)]
    list_min = 33
    list_i = [0 for _ in range(N)]
    wornl(0,N,0)
    print('#{0} {1}'.format(tc+1, list_min))