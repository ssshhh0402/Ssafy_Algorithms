def find(tg_s, tg_e):          #find(시작점배열, 끝점 배열, 타겟_시작점, 타겟_끝점)
    if tg_s == tg_e:                                            #
        return 1

    for i in range(len(list_S)):                    #만약 끝 리스트에 있는 값이랑 입력받는 값(th_e)와 같다면
        if list_E[i] == tg_e:
            if find(tg_s, list_S[i]):
                return 1
    return 0


for tc in range(int(input())):
    list_S = []
    list_E = []
    V, E = map(int, input().split())

    for i in range(E):
        u, v = map(int, input().split())
        list_S.append(u)
        list_E.append(v)
    t_S, t_E = list(map(int, input().split()))
    print('#{0} {1}'.format(tc+1, find(t_S, t_E)))
