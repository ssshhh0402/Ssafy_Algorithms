#md 1: 위로
#md 2: 오른쪽
#md 3: 왼쪽
import sys
sys.stdin = open('ladder.txt', 'r')

def find(arr, x, y, md):
    if x == 0 :
        return y
    else:
        if md == 1:
            if y == 0:
                while True:
                    x -= 1
                    if x == 0:
                        return y
                    if arr[x][y+1] == 1 :
                        break
                return find(arr, x, y, 2)
            elif y == 99:
                while True:
                    x -= 1
                    if x == 0:
                        return y
                    if arr[x][y-1] == 1:
                        break
                return find(arr, x, y, 3)
            else:
                while True:
                    x -= 1
                    if x == 0:
                        return y
                    elif arr[x][y + 1] == 1 or arr[x][y - 1] == 1:
                        break
                if arr[x][y+1] == 1:
                    return find(arr, x, y, 2)
                elif arr[x][y-1] == 1:
                    return find(arr, x, y, 3)
        elif md == 2:
            while True:
                y += 1
                if arr[x-1][y] == 1:
                    break
            return find(arr, x, y, 1)
        elif md == 3:
            while True:
                y -= 1
                if arr[x-1][y] == 1:
                    break
            return find(arr, x, y, 1)


for case in range(10):
    tc = int(input())
    base = []
    x = 99
    y = 0
    for i in range(100):
        base.append(list(map(int, input().split())))

    for j in range(100):
        if base[x][j] == 2:
            y = j
            break
    print('#{0} {1}'.format(tc, find(base, x, y, 1)))