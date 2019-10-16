V, E = map(int, input().split())            #V = 정점 수 ,E = 간선 수
Edge = [tuple(map(int, input().split())) for _ in range(E)] #(u,v,w)

p = [x for x in range(V)]


def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


Edge.sort(key=lambda x : x[2])  # 가중치를 기준으로 오름차순 정렬
MST = []
idx = 0
while len(MST) < V-1:
    u,v,w = Edge[idx]
    a = find_set(u)
    b = find_set(v)
    if a != b:
        MST.append((u,v,w))
        p[b] = a
    idx += 1

print(*MST)
