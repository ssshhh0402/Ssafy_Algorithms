for tc in range(1, int(input())+1):
    N = int(input())
    base = list(map(int, input().split()))
    visit = [0]*((100*N)+1)
    for i in range(1 << N):
        imsi = 0
        for j in range(N+1):
            if i & 1 << j:
                imsi += base[j]
            print(imsi)
        visit[imsi] = 1
    print("#{0} {1}".format(tc, sum(visit)))