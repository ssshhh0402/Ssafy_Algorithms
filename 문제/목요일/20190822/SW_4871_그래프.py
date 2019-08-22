# def find(arr_s, arr_e, tg_s, tg_e):          #find(시작점배열, 끝점 배열, 타겟_시작점, 타겟_끝점)
#     for i in range(len(arr_e)):
#             if arr_e[i] == tg_e:               # 끝점에서 타겟과 동일한 아이 찾아서
#                 if arr_s[i] == tg_s:              #같은 인덱스의 시작점 값과 타겟 시작점 같다면 끝
#                     return 1
#                 elif arr_s[i] in arr_e:            #같은 인덱스의 시작점 값이 끝점 배열에 존재한다면 다시 호출
#                     return find(arr_s, arr_e, tg_s, arr_s[i])
#                 else:                              # 만약 존재하지 않을 경우 계속 진행
#                     continue
#     else:                                           #중간에 안멈추고 계속 돌았을 경우 없다는 뜻이기때문에 존재 x
#         return 0
#
def find(arr_s, arr_e, tg_s, tg_e):          #find(시작점배열, 끝점 배열, 타겟_시작점, 타겟_끝점)
    if tg_s == tg_e: return 1

    for i in range(len(arr_e)):
            if arr_e[i] == tg_e:               # 끝점에서 타겟과 동일한 아이 찾아서
                return find(arr_s, arr_e, tg_s, arr_s[i])
                                                    #중간에 안멈추고 계속 돌았을 경우 없다는 뜻이기때문에 존재 x
    return 0


for tc in range(int(input())):
    list_S = []
    list_E = []
    V, E = list(map(int, input().split()))
    for i in range(E):
        S, E = list(map(int, input().split()))
        list_S.append(S)
        list_E.append(E)
    t_S, t_E = list(map(int, input().split()))
    print('#{0} {1}'.format(tc+1, find(list_S, list_E, t_S, t_E)))