m, n = 4, 3
puddles = [[2,2]]
base = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in puddles:
    base[i[0]][i[1]] = -1
for i in range(1, n+1):
    for j in range(1, m+1):
        if base[i][j] < 0:
            continue
        elif i == 1:
            base[i][j] = 1
        elif j == 1:
            base[i][j] = 1

        else:
            if base[i-1][j] < 0:
                base[i][j] = base[i][j-1]
            elif base[i][j-1] < 0:
                base[i][j] = base[i-1][j]

            else:
                base[i][j] = base[i-1][j] + base[i][j-1]
print(base[n][m] % 1000000007)