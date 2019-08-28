def jg(start, end):
    if start + 1 == end:
        return win(start, end)
    elif start == end:
        return start
    else:
        num_1 = jg(start,(start + end) // 2)
        num_2 = jg(((start+ end) // 2)+1, end)
        return win(num_1, num_2)

def win(a, b):
    if std[a] == 1:
        if std[b] == 3:
            return a
        elif std[b] == 1:
            return a
        else:
            return b
    elif std[a] == 2:
        if std[b] == 1:
            return a
        elif std[b] == 2:
            return a
        else:
            return b
    elif std[a] == 3:
        if std[b] == 2:
            return a
        elif std[b] == 3:
            return a
        else:
            return b

for tc in range(int(input())):
    N = int(input())
    std = list(map(int, input().split()))
    print('#{0} {1}'.format(tc+1, jg(0, N-1)+1))
