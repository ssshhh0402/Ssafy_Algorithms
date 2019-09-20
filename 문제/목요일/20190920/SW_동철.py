def find(a, b): #a = 일한 사람 수 b = 확률 계산
    global result
    if a == N:
        result = max(result, b)
        return
    elif b <= result:
        return
    for i in range(N):
        if not worked[i]:
            worked[i] = 1
            find(a+1, b * (base[a][i]/100))
            worked[i] = 0



for tc in range(1, int(input())+1):
    N = int(input())
    base = [list(map(int,input().split())) for _ in range(N)]
    worked = [0 for _ in range(N)]
    result = 0
    for i in range(N):
        worked[i] = 1
        find(1, base[0][i] / 100)
        worked[i] = 0

    print("#{0} {1:.6f}".format(tc, result * 100))