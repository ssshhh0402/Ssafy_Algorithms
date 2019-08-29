for case in range(10):
    tc = int(input())
    base = []
    str = list(map(int, input().split()))
    for i in range(len(str), 100):
        base.append(str[i:i+100])
    print(base)