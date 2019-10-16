def find(a,b,c,d):    #a = 횟수, b = 왼쪽, c = 오른쪽, d = 곱하기 눌렀냐(b * c 일때)
    global min_n, flag, flag_2
    if b*c == N:
        min_n = min(min_n, a)
        return
    if b*c > N:
        return
    elif a >= min_n:
        return
    if used[b*c]:
        return
    used[b*c] = 1
    for i in list_p:
        if not d:
            find(a+1, b * 10 + i, c, d)         #b에 붙일때
            find(a+2, b, c*i, 1)             # 곱하기 눌렀을 때
        else:
            find(a+2, b * c, i, d)          #곱하기 눌렀을 때
            find(a+1, b, c * 10 + i, d)     #c에 붙일때


for tc in range(1, int(input())+1):
    base = list(map(int, input().split()))
    N = int(input())
    flag = 0
    used = [0 for _ in range(N+1)]
    list_p = []
    min_n = 0xffffff
    for i in range(10):
        if base[i]:
            list_p.append(i)
    for j in list_p:
        find(1,j,1,0)
        used = [0 for _ in range(N+1)]
    if min_n == 0xffffff:
        print("#{0} {1}".format(tc, -1))
    else:
        print("#{0} {1}".format(tc, min_n + 1))