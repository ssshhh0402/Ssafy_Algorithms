def paint(arr, list_x, list_y, color):
    for j in range(list_x[0], list_x[1]+1, 1):
        for q in range(list_y[0], list_y[1]+1, 1):
            arr[j][q] = color



def c_color(arr):
    
    #c_list = [0 for _ in range(11)]
    for i in range(N):
        for j in range(N):
            c_list[arr[i][j]] += 1
    return max(c_list)


def can_p(arr, list_x, list_y, color):
    for j in range(list_x[0], list_x[1]+1, 1):
        for q in range(list_y[0], list_y[1]+1, 1):
            if arr[j][q] > color:
                return False
    else:
        return True


for tc in range(int(input())):
    N, M, K = map(int, input().split())
    base = [[0 for _ in range(N)] for _ in range(M)]
    c_list = [0 for _ in range(11)]
    for _ in range(K):
        order = list(map(int, input().split()))
        list_x = [order[x] for x in range(4) if x % 2 == 0]
        list_y = [order[x] for x in range(4) if x % 2 != 0]
        color = order[-1]
        if can_p(base, list_x, list_y, color):
            paint(base, list_x, list_y, color)
    print('#{0} {1}'.format(tc+1, c_color(base)))

