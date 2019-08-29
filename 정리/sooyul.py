arr = 'ABC'
N = len(arr)

order = [0] * N #실제 요소들의 순서(index를 기록)


def perm(k, n, used):
    if k == n:
        for j in range(N):
            print(arr[order[j]], end=' ')
            print()
            return


    used = [False] * N   #지금까지 선택한 원소들의 집합
    for i in range(N):
        used[order[i]] = True
    for i in  range(N):
        if used & (1 << i) :
            continue
        order[k] = i
        perm(k + 1, n, used | (1 << i))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if i == k or j == k:
                continue
            print(arr[i], arr[j], arr[k])


# def per(k, n, used, cursum):
#     if k == n:
#         MIN = cursum
#
#     for i in range(n):
#         if used & (1 << i): continue
#             per(k+1, n ,used | (1 << i), cursum + arr[k])
                ## By 강사님
