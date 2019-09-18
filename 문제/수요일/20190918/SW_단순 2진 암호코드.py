
def change(arr):
    if arr == [0,0,0,1,1,0,1]:
        return 0
    elif arr == [0,0,1,1,0,0,1]:
        return 1
    elif arr == [0,0,1,0,0,1,1]:
        return 2
    elif arr == [0,1,1,1,1,0,1]:
        return 3
    elif arr == [0,1,0,0,0,1,1]:
        return 4
    elif arr == [0,1,1,0,0,0,1]:
        return 5
    elif arr == [0,1,0,1,1,1,1]:
        return 6
    elif arr == [0,1,1,1,0,1,1]:
        return 7
    elif arr == [0,1,1,0,1,1,1]:
        return 8
    elif arr == [0,0,0,1,0,1,1]:
        return 9







for tc in range(int(input())):
    cod = []
    N, M = list(map(int, input().split()))
    base = [list(map(int,input())) for _ in range(N)]
    flag = 0
    for i in range(0,N,1):
        a = []
        y_flag = 0
        for j in range(M-1,-1,-1):
            if y_flag:
                a.append(base[i][j])
                if len(a) == 7:
                    b = change(list(reversed(a)))
                    if b is not None:
                        cod.append(b)
                        y_flag = 0
                        a.clear()
            elif base[i][j] == 1:
                flag = 1
                y_flag = 1
                a.append(base[i][j])
        if flag:
            break
    sum_h = 0
    sum_j = 0
    cod = list(reversed(cod))
    for i in range(0,7):
        if (i+1) % 2 == 0:
            sum_j += cod[i]
        else:
            sum_h += cod[i]
    result = 3 * sum_h + sum_j + cod[7]
    if result % 10 == 0:
        print("#{0} {1}".format(tc+1, sum(cod)))
    else:
        print("#{0} 0".format(tc+1))
