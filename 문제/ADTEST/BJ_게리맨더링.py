# 하나씩 증가해 가면서 좌우 나누고
# 좌우 연결 되어있으면 인굿수 추가
# 이렇게 풀면 안되는 걸로 ㅎㅎ
from collections import deque
def connected(arr): # 안엥 있는 요소들이 연결되어 있나 확인
    global G
    if not arr:
        return 0
    visited = [0 for _ in range(N + 1)]
    stck = deque([arr[0]])
    visited[arr[0]] = 1
    while stck:
        n = stck.popleft()
        for j in G[n]:
            if not visited[j] and j in arr:
                stck.append(j)
                visited[j] = 1
    if len(arr) == visited.count(1):
        return 1
    else:
        return 0


def calc(arr): #안에 있는 요소들의 합 반환
    sum = 0
    for j in arr:
        sum += people[j]
    return sum


def find(arr_1, arr_2): #arr_1 = 좌 집합 arr_2 = 우 집합
    global result, flag
    if connected(arr_1) and connected(arr_2):
        person = abs(calc(arr_1) - calc(arr_2))
        result = min(person, result)
        flag = True
        return

    for i in range(len(arr_1)):
        imsi = arr_1.pop(i)
        arr_2.append(imsi)
        find(arr_1, arr_2)
        arr_1.insert(i,arr_2.pop())




N = int(input())
people = list(map(int, input().split()))
people.insert(0,0)
base = [x for x in range(1, N+1)]
result = 0xffffff
flag = False
G = [ set() for _ in range(N+1)]
for idx in range(1,N+1):
    arr = list(map(int, input().split()))
    for j in range(1,1+arr[0]):
        G[idx].add(arr[j])
        G[arr[j]].add(idx)
find(base, [])

if not flag:
    print('-1')
else:
    print(result)