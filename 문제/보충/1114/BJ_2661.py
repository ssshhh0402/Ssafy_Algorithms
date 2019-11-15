def pos(b):                         # 착한 수열인지 확인
    n = len(b)
    same = True
    m = n // 2
    for i in range(1, m + 1):
        x = b[-i:]
        y = b[-2 * i: -i]
        if x == y:
            same = False
            break

    return same


def find(a, b):     #a : 사용한 갯수, b : 판
    global result
    if not pos(b):
        return

    if a == N:
        num = int(''.join(b))
        result = min(result, num)
        return

    for i in range(1, 4):
        b.append(str(i))
        find(a+1, b)
        b.pop()




N = int(input())
base = []
result = 0xffffff
for i in range(1, 4):
    base.append(str(i))
    find(1,base)
    base.pop()
print(result)