from collections import deque


def Big(a):
    stck = deque([a])
    visit = [0 for _ in range(N+1)]
    visit[a] = 1
    big = -1
    while stck:
        for _ in range(len(stck)):
            x = stck.popleft()
            big +=1
            for item in G[x]:
                if not visit[item]:
                    stck.append(item)
                    visit[item] = 1
    return big

def Small(a):
    stck = deque([a])
    visit = [0 for _ in range(N+1)]
    visit[a]= 1
    small = -1
    while stck:
        for _ in range(len(stck)):
            x = stck.popleft()
            small += 1
            for item in g[x]:
                if not visit[item]:
                    stck.append(item)
                    visit[item] =1

    return small

for tc in range(1, int(input())+1):
    N = int(input())
    M = int(input())
    G = [[] for _ in range(N+1)]         # G[i] = j => i에 있는 얘보다 큰 애 = j
    g = [[] for _ in range(N+1)]            # g[i] = j => i에 있는 얘보다 작은 애 = j
    answer = 0
    for _ in range(M):
        a, b = list(map(int,input().split()))
        G[a].append(b)
        g[b].append(a)

    for i in range(1, N+1):
        bigger = Big(i)
        lower = Small(i)
        if bigger + lower == N-1:
            answer += 1

    print("#{0} {1}".format(tc, answer))