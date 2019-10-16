from collections import deque
def find(a):
    global matched,result
    stck = deque([a])
    matched[a] = 1
    while stck:
        n = stck.popleft()
        for v in G[n]:
            if not matched[v]:
                matched[v] = 1
                stck.append(v)


for tc in range(1, int(input())+1):
    N, M = map(int,input().split())
    G = [[] for _ in range(N+1)]
    matched = [0 for _ in range(N+1)]
    imsi = list(map(int,input().split()))
    for idx in range(0,len(imsi),+2):
        g, v = imsi[idx], imsi[idx+1]
        G[g].append(v)
        G[v].append(g)
    result = 0
    for i in range(N+1):
        if G[i] and not matched[i]:
            find(i)
            result += 1
    print("#{} {}".format(tc, result+matched.count(0)-1))