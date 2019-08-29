for tc in range(int(input())):
    N, M = map(int,input().split())
    base = list(map(int, input().split()))
    for _ in range(M):
        base.append(base.pop(0))
    print('#{0} {1}'.format(tc+1,base[0]))