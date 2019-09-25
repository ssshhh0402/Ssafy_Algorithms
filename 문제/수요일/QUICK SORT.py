arr = [69, 10, 30, 2, 16, 8, 31, 22]


def quicksort(lo, hi):
    if lo >= hi:
        return
    i, j = lo, hi
    while i < j:
        while i <= hi and arr[lo] >= arr[i]:
            i += 1
        while arr[lo] < arr[j]:
            j-= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        arr[lo], arr[j] = arr[j], arr[lo]
        quicksort(lo, j-1)
        quicksort(j+1,hi)

print(arr)
quicksort(0,len(arr) -1)
print(arr)