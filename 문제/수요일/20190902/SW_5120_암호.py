for tc in range(int(input())):
    N, M, K =  map(int, input().split())
    base = list(map(int, input().split()))
    flag = 0
    for _ in range(K):
        if flag + M < len(base):
            flag = flag + M
            base.insert(flag, base[flag - 1] + base[flag])
        elif flag + M == len(base):
            flag = flag + M
            base.append(base[flag-1] + base[0])
        else:
            flag = (flag + M) % (len(base))
            base.insert(flag, base[flag - 1] + base[flag])

    print('#{0}'.format(tc+1),end=" ")
    if len(base) > 10:
        for i in range(len(base)-1, len(base)-11,-1):
            print(base[i], end=" ")
    else:
        for i in range(len(base)-1, -1, -1):
            print(base[i], end=" ")
    print("")