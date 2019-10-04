def find(a,b,c):    #a = 횟수, b = 합 c = 곱했냐
    global min_n, flag
    if b == N:
        min_n = min(min_n, a)
        if not flag:
            flag = 1
        return
    if b > N:
        return
    elif a >= min_n:
        return
    if used[b]:
        return
    used[b] = 1
    for i in list_p:
        if not c:
            find(a+1, b * 10 + i, c)
        find(a+2, b * i, 1)

for tc in range(1, int(input())+1):
    base = list(map(int, input().split()))
    N = int(input())
    used = [0 for _ in range(N+1)]
    flag = 0
    list_p = []
    min_n = 0xffffff
    for i in range(10):
        if base[i]:
            list_p.append(i)
    for j in list_p:
        find(1,j,0)
        used = [0 for _ in range(N+1)]
    if not flag:
        print("#{0} {1}".format(tc, -1))
    else:
        print("#{0} {1}".format(tc, min_n + 1))