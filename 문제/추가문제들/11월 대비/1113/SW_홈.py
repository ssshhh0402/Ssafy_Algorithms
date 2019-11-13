def find(a,b):
    global result, count
    for k in range(1, 2*N):
        cnt = 0
        if k == 1:
            if base[a][b] == 1:
                cnt += 1
        else:
            # for x in range(a+2-k,a+k-1,1):
            #     for y in range(b+2-k, b+k-1, 1):
            #         if 0 <= x < N and 0 <= y < N:
            #             if base[x][y] == 1:
            #                 cnt += 1
            # for x, y in [(a-k+1, b), (a+k-1, b), (a, b-k+1), (a, b+k-1)]:
            #     if 0 <= x < N and 0 <= y < N:
            #         if base[x][y] == 1:
            #             cnt += 1
            for i in range(k):
                for p in range(-k+i+1, k-i+1):
                    x, y = a-i, b+p
                    if 0 <= x < N and 0 <= y < N:
                        if base[x][y] == 1:
                            cnt += 1
        byong = k ** 2 + (k-1) ** 2
        income = M * cnt
        ed = income - byong
        if ed >= 0:
            count = max(count, cnt)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    base = [list(map(int,input().split())) for _ in range(N)]
    homes = []
    count = -0xfffffff

    for i in range(N):
        for j in range(N):
            find(i,j)
    print("#{0} {1}".format(tc, count))