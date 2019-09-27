def binarySearch(arr, key):
    lo, hi = 0, len(arr) - 1
#lo = 범위 시작, hi = 범위 끝

    while lo <= hi:
        mid = (lo+hi) >> 1 #bit 연산자를 사용한 연산( / 2)
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1
        return False

def selection (list, k):
    for i in range(len(list)):
        min_I = i
        for j in range(i+1, len(list)):
            if list[min_I] < list[j]:  #최 소값이니까 더 작은 아이를 저장
                min_I = j

        list[i], list[min_I] = list[min_I], list[i]

    return list[k-1]


print(selection([64,25,10,22,11],5))