Arr = ['a','b','c','d','e','f']
N = len(Arr)
result = []
for i in range(1 << N):
    imsi = []
    for j in range(N+1):
        if i & (1 << j):
            imsi.append(Arr[j])
    if len(imsi) == 2:
        result.append(''.join(imsi))
print(len(result))
print(result)