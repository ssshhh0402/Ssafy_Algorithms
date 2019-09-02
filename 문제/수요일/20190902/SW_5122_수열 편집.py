for tc in range(int(input())):
    N, M, L = map(int,input().split())
    base = list(map(int, input().split()))
    for _ in range(M):
        order = list(input().split())
        if order[0] == 'I':
            base.insert(int(order[1]),int(order[2]))
        elif order[0] == 'D':
            for idx in range(int(order[1]),len(base)-1):
                base[idx] = base[idx+1]
            base.pop()
        elif order[0] == 'C':
            base[int(order[1])] = int(order[2])
    if len(base) <= L:
        print('#{0} -1'.format(tc+1))
    else:
        print('#{0} {1}'.format(tc+1, base[L]))