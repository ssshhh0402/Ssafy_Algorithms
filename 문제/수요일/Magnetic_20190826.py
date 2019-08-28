import sys
sys.stdin = open('input.txt', 'r')
for tc in range(10):
    gil = int(input())
    stc = []
    count = 0
    base = []
    for case in range(gil):
        base.append(list(map(int, input().split())))
                                                                # 1이면 아래로 2면 위로
    for y in range(gil):
        stc.clear()
        for x in range(gil-1, -1, -1):
            if base[x][y] == 2:
                stc.append(2)
            elif base[x][y] == 1:
                if len(stc) == 0:
                    continue
                else:
                    if stc[-1] == 2:
                        count += 1
                    while True:
                        if len(stc) == 0:
                            break
                        else:
                            stc.pop()
                    #stc.append(1)
    print('#{0} {1}'.format(tc+1, count))

