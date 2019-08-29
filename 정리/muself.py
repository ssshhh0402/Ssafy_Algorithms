arr = [1,2,3,4,5,6]
n = len(arr)
result = []
for i in range(1 << n):
    imsi = [i]
    for j in range(n+1):
        if i & (1 << j):
            imsi.append(j)
    result.append(imsi)
print(result)