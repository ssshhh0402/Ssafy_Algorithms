def find(a, b, c):      #a = 시작 하는 방 b = 들어간 방 갯수 c = 사용한 에너지
    global result
    if b == N:
        result= min(result,c)
        return
    elif c > result:
        return
    if b == N-1:
        for i in range(N):
            if base[a][i] and not visited[i]:
                visited[i] = 1
                start, visit = a, i
                find(i,b+1, c + base[a][i])
                visited[i] = 0
    else:
        for i in range(1, N):
            if base[a][i] and not visited[i]:
                visited[i] = 1
                start, visit = a, i
                find(i,b+1, c + base[a][i])
                visited[i] = 0




for tc in range(1, int(input())+1):
    N = int(input())
    base = [list(map(int, input().split()))for _ in range(N)]
    visited = [0 for _ in range(N)]
    result = 0xffffff
    find(0, 0, 0)
    print("#{0} {1}".format(tc,result))