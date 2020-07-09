N = int(input())
base = [[ 0 for _ in range(2)] for _ in range(N)]
result = ['' for _ in range(N)]
for idx in range(N):
    k, h = map(int, input().split())
    base[idx][0] = k
    base[idx][1] = h

for idx in range(N):
    count = 0
    for others in range(N):
        if base[idx][0] < base[others][0] and base[idx][1] < base[others][1]:
            count += 1
    result[idx] = str(count + 1)

print(' '.join(result))