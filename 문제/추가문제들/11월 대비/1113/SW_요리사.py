def calc(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                imsi = base[a[i]][a[j]]
                count += imsi
    return count


def find(a, b):
    global result
    food_1 = calc(a)
    food_2 = calc(b)
    result = min(result, abs(food_1 - food_2))


for tc in range(1, int(input())+1):
    N = int(input())
    base = [list(map(int,input().split()))for _ in range(N)]
    jaeryo = [x for x in range(1, N+1)]
    result = 0xffffff
    for i in range(1 << N):
        base_a = []
        base_b = []
        for j in range(N):
            if i & (1 << j):
                base_a.append(jaeryo[j]-1)
            else:
                base_b.append(jaeryo[j]-1)
        if len(base_a) == (N // 2) and len(base_b) == (N //2):
            find(base_a, base_b)
    print("#{0} {1}".format(tc, result))