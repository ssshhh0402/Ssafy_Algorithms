def mergeSort(lo, hi):
    global count
    if hi-lo == 0:
        return
    mid = (lo+hi) >> 1
    mergeSort(lo,mid)
    mergeSort(mid+1,hi)
    i,j,k = lo, mid+1, lo
    if base[i-1] > base[k-1]:
        count += 1
    while i <= mid and j <= hi:
        if base[i] < base[j]:
            result[k] = result[i]
            i += 1
            k += 1
        else:
            result[k] = base[j]
            j += 1
            k += 1
    while i <= mid:
        result[k] = base[i]
        k, j = k+1, j+1
    while j <= hi:
        result[k] = base[j]
        k, j = k+1, j+1


for tc in range(1, int(input())+1):
    N = int(input())
    count = 0
    result = [0 for _ in range(N)]
    base = list(map(int, input().split()))
    mergeSort(0,len(base)-1)
    print("#{0} {1} {2}".format(tc, base[N//2], count))