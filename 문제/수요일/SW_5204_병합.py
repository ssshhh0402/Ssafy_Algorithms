def hapchim(arr_1, arr_2):
    imsi = []
    while arr_1 and arr_2:
        if arr_1[0] < arr_2[0]:
            imsi.append(arr_1.pop(0))
        else:
            imsi.append(arr_2.pop(0))
    if arr_1:
        while arr_1:
            imsi.append(arr_1.pop(0))
    else:
        while arr_2:
            imsi.append(arr_2.pop(0))
    return imsi


def binary(arr):
    global count
    lo = 0
    hi = len(arr)
    mid = (lo + hi) // 2
    if lo == mid:
        return arr
    arr_1 = binary(arr[lo:mid])
    arr_2 = binary(arr[mid:hi])
    if arr_1[-1] > arr_2[-1]:
        count += 1



for tc in range(1, int(input())+1):
    N = int(input())
    count = 0
    base = list(map(int, input().split()))
    base = binary(base)
    print("#{0} {1} {2}".format(tc, base[N//2], count))