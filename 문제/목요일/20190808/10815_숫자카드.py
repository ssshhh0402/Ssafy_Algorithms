
def find(a, b, c, d):    #a = 배열, b = 찾는 값 c = 처음 d = 마지막
    while c <= d:
        mid = (c + d) // 2
        if a[mid] == b:
            return True
        elif a[mid] < b:
            c = mid + 1
        else:
            d = mid - 1
    return False


num_a = int(input())
sang = list(map(int, input().split()))
num_b = int(input())
answer = list(map(int, input().split()))
sang.sort()
for i in answer:
    if find(sang, i, 0, num_a-1):
        print('1', end=" ")
    else:
        print("0", end=" ")
