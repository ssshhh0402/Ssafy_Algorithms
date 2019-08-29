import sys;
sys.stdin=open('DFS_input.txt', 'r')

def DFS(v):
    # 시작점 방문 스택 push
    # 빈 스택이 아닐 동안 반복
    # v의 방문하지 않은 인정점접 w를 찾는다
    # w를 찾아서 방문하고 v를 스택에 push
    # v를 w로 설정한다.
    # 만약 인접 정점이 없다면, 스택에서 pop()해서 v로 설정
    # v는 현재 방ㅂ문하는 접점

    S = []
    visit[v] = True
    S.append(v)
    while S:                #빈스택이 아닐 동안
        for w in G[v]:
            if not visit[w]:            #v의 방문핮 ㅣ않은 인접정보 탐색
                    visit[w] = True
                    S.append(v)              # w를 방문하고,
                    v = w
                    break# v를 w로 설정
        else:
            v = S.pop()


V, E = map(int, input().split())

G = [[]for _ in range(V + 1)]  #1~V 번 까지
visit = [False] * (V + 1)

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[u].append(u)

