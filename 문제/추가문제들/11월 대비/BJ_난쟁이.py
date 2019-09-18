def find(a, b):     #명수, 키 합
    global flag, checked
    if a == 7 and b == 100:
        flag = True
        return
    for i in range(9):
        if not checked[i] and b + base[i] <= 100 :
            checked[i] = 1
            result.append(base[i])
            find(a+1, b + base[i])
            if flag:
               break
            else:
                checked[i] = 0
                result.pop()

base = []
result = []
flag = False
for _ in range(9):
    base.append(int(input()))
checked = [0 for _ in range(9)]
for i in range(9):
    checked[i] = 1
    result.append(base[i])
    find(1,base[i])
    if flag:
        break
    else:
        checked[i] = 0
        result.pop()
result = sorted(result)
for i in result:
    print(i)