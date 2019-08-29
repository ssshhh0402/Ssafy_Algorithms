# 하나씩 x 값 변경해가면서
# 직접 돌려보고
# 정렬이 되면 1 반환
# 없되면 -1 반환
# count가 5 이상 되면 끝
# 저거 조건문에 넣어서
# 카운트 비교해서 더 작은수를 반환


def is_ordered(arr):
    if arr[0] > arr[len(arr)-1]:
        for i in range(len(arr)-1):
            if arr[i] - 1 != arr[i+1]:
                return 0
        else:
            return 1
    elif arr[len(arr)-1] > arr[0]:
        for i in range(len(arr)):
            if arr[i] + 1 != arr[i+1]:
                return 0
        else:
            return 1


def up(arr, a):
    global min_c, N
    arr_m = []
    if a >= 6:
        return 0
    elif is_ordered(arr):
        if min_c < a:
            min_c = a
        return 1
    else:
        for x in range(0, N-1):
            arr_1 = list(arr[0,N//2])
            arr_2 = list(arr[N//2+1, N])
            if x < N//2:
                for y in range(N // 2 - x):
                    arr_m.append(arr_1.pop(0))
                while arr_1 and arr_2:
                    arr_m.append(arr_2.pop(0))
                    arr_m.append(arr_1.pop(0))
                if not arr_2:
                    while len(arr_2) != 0:
                        arr_m.append(arr_2.pop(0))
            elif x == N // 2:
                while arr_1:
                    arr_m.append(arr_2.pop(0))
                    arr_m.append(arr_1.pop(0))
            else:
                while len(arr_m) != x - N +1 :
                    arr_m.append(arr_2.pop(0))
                while len(arr_2) != 0:
                    arr_m.append(arr_1.pop(0))
                    arr_m.append(arr_2.pop(0))
                while len(arr_1) != 0:
                    arr_m.append(arr_1.pop(0))
            if up(arr_m, a+1):
                return 1


for tc in range(int(input())):
    N = int(input())
    base = list(map(int, input().split()))
    min_c = 0
    if up(base, 0):
        print('#{0} {1}'.format(tc+1, min_c))
    else:
        print('#{0} -1'.format(tc+1))