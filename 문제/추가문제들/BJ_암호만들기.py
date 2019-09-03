def check(arr):
    list_check = ['a', 'e', 'i', 'o', 'u']
    c_ja = 0
    c_mo = 0
    for item in arr:
        if item in list_check:
            c_mo += 1
        else:
            c_ja += 1
    if c_mo >= 1 and c_ja >= 2:
        return True
    else:
        return False


def dic_order(arr):
    gyulgwa = True
    for index in range(len(arr)-1):
        if ord(arr[index]) > ord(arr[index+1]):
            gyulgwa = False
            break
    return gyulgwa


N, M = map(int, input().split())
base = sorted(list(input().split()))
result = []
for i in range(1 << len(base)):
    imsi = []
    for j in range(len(base)+1):
        if i & (1 << j):
            imsi.append(base[j])
    if len(imsi) == N:
        result.append(imsi)
result.sort()
for idx in range(len(result)):
    if check(result[idx]) and dic_order(result[idx]):
        print(''.join(result[idx]))
