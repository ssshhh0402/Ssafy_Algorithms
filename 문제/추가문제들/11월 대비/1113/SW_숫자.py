def find(a,b):      # a = 여태까지 계산한 값 , b = 사용한 연산자 갯수
    global result_ax,result_in, ope
    if b == N:
        result_ax = max(result_ax, a)
        result_in = min(result_in, a)
        return
    for i in range(4):
        if ope[i] != 0:
            ope[i] -= 1
            if i == 0:
                find(a+numbers[b], b+1)
            elif i == 1:
                find(a - numbers[b], b+1)
            elif i == 2:
                find(a * numbers[b], b+1)
            else:
                find(int(a / numbers[b]), b+1)
            ope[i] += 1


for tc in range(1, int(input())+1):
    N = int(input())
    ope = list(map(int,input().split()))
    numbers = list(map(int,input().split()))
    result_ax = -0xffffff
    result_in = 0xffffff
    find(numbers[0],1)
    print("#{0} {1}".format(tc, result_ax - result_in))