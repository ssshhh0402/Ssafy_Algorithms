import sys
sys.stdin = open('node.txt','r')


def find(a):
    global m_min
    visited = [0] * (N+1)
    qu = []
    length = [0] * (N+1)
    visited[a] = 1
    qu.append(a)

    result = []
    while qu:
        w = qu.pop(0)
        for g in G[w]:
            if not visited[g]:
                visited[g] = 1
                qu.append(g)
                length[g] = length[w] + 1
                m_min = max(length[g], m_min)
    for idx in range(N+1):
        if length[idx] == m_min:
            result.append(idx)
    return max(result)


for tc in range(10):
    N, S = map(int, input().split())
    G = [[] for _ in range(N+1)]
    m_min = 0
    base = list(map(int, input().split()))
    for idx in range(0, len(base), +2):
        s = base[idx]
        v = base[idx+1]
        if v not in G[s]:
            G[s].append(v)
    print('#{0} {1}'.format(tc+1, find(S)))

