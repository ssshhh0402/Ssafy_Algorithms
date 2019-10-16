def find(x):
    if x != P[x]:
        P[x] = find(P[x])
    return P[x]


for tc in range(1, int(input())+1):
    V, E = map(int,input().split())
    G = [list(map(int, input().split())) for _ in range(E)]
    G.sort(key =lambda x: x[2])
    P = [x for x in range(V+1)]
    idx = 0
    result = 0
    while idx != V:
        u,v,w = G[idx]
        a = find(u)
        b = find(v)
        if a != b:
            result += w
            P[b] = a

        idx += 1
    print("#{} {}".format(tc, result))