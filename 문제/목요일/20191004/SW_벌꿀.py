def pos(a,b):   # a,b = 위치, (a,b)가 가능한지 아닌지 판단하는 함수 가능하면 1 아니면 0
    if b > N-M:
        return 0
    elif not any(visited[a][b+x] for x in range(M)):
        return 1
    else:
        return 0


def hap(a,b):   #a,b = 위치 , 범위 안에 있는 애들의 최고 값 반환하는 함수
    imsi = [base[a][x] for x in range(b,b+M)]
    tong = []
    sum_num = 0
    for i in range(1 << M):
        imsi_2 = []
        for j in range(M+1):
            if i & (1 << j):
                imsi_2.append(imsi[j])
        if sum(imsi_2) <= C:
            if imsi_2 not in tong:
                tong.append(imsi_2)
        else:
            index = 0
            i_sum = 0
            imsi_2 = sorted(imsi_2)
            for i in range(len(imsi_2)):
                if i_sum + imsi_2[i] <= C:
                    i_sum += imsi_2[i]
                    index = i
                else:
                    break
            ans = imsi_2[0:index+1]
            if ans not in tong:
                tong.append(ans)
    for i in tong:
        imsi_num = 0
        for j in i:
            imsi_num += j**2
        sum_num = max(sum_num, imsi_num)
    return sum_num


def find(a,b):  # a = 갯수 b = 합
    global result
    if a == 2:
        result = max(result, b)
        return
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and pos(i,j):
                for q in range(M):
                    visited[i][j + q] = 1
                find(a+1, b+hap(i,j))
                for q in range(M):
                    visited[i][j + q] = 0


for tc in range(1, int(input())+1):
    N,M,C = map(int,input().split())
    base = [list(map(int,input().split()))for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N-M+1):
            for q in range(M):
                visited[i][j+q] = 1
            find(1, hap(i,j))
            for q in range(M):
                visited[i][j+q] = 0

    print("#{} {}".format(tc, result))