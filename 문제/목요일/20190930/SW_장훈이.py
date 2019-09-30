def find(a, b):     #a = 인덱스. b = 차이
    global result
    if b >= 0:
        result = min(result, b)
        return
    for i in range(a+1, N):
        find(i, b+base[i])


for tc in range(1, int(input())+1):
    N,B = map(int, input().split())
    base = list(map(int,input().split()))
    result = 0xffffff
    for i in range(N):
        find(i,base[i] - B)
    print("#{0} {1}".format(tc, result))