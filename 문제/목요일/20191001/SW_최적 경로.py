def find(a,b,c,d):      #a = x좌표 ,b = y좌표, c = 거리 d = 들린 고객 집
    global result
    if d == N:
        home = abs(a-home_x) + abs(b - home_y)
        result = min(c + home, result)
        return
    if c >= result:
        return
    for i in range(len(c_list)):
        if not visit[i]:
            imsi = abs(c_list[i][0] - a) + abs(c_list[i][1] - b)
            visit[i] = 1
            find(c_list[i][0],c_list[i][1], c + imsi, d+1)
            visit[i] = 0




for tc in range(1, int(input())+1):
    N = int(input())
    base = list(map(int, input().split()))
    c_list = []
    result = 0xffffff
    ssafy_x, ssafy_y = base[0:2]
    home_x, home_y = base[2:4]
    D = [[0 for _ in range(N+1)] for _ in range(N+1)]           #집 간의 거리 예시 함수안에서 현재 집 몇번째 집인지 받으면 될듯
    for i in range(4, len(base)-1,2):
        c_x, c_y = base[i],base[i+1]
        c_list.append((c_x, c_y))
    visit = [0 for _ in range(len(c_list))]
    for c in range(len(c_list)):
        for j in range(len(c_list)):
            if c != j:
                d = abs(c_list[c][0] - c_list[j][0]) + abs(c_list[c][1] - c_list[j][1])
        D[c][j] = D[j][c] = d
    print(D)

    for i in range(N):
        d = abs(c_list[i][0] - ssafy_x) + abs(c_list[i][1] - ssafy_y)
        visit[i] = 1
        find(c_list[i][0],c_list[i][1],d,1)
        visit[i] = 0
    print("#{0} {1}".format(tc, result))