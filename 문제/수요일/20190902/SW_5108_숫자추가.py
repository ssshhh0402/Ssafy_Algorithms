def add(idx, v):
    global base
    base.append(0)
    for i in range(len(base)-1, idx,-1):
        base[i] = base[i-1]
    base[idx] = v


def m_print(idx):
    global base
    return base[idx]











for tc in range(int(input())):
    N, M, L = map(int, input().split())
    base = list(map(int, input().split()))
    for M in range(M):
        add_I, add_N = map(int, input().split())
        add(add_I, add_N)
    print('{0} {1}'.format(tc+1, m_print(L)))
