for tc in range(int(input())):
    base = list(input().split())
    N = len(base)
    num = []
    for i in range(N):
        if base[i].isdigit():
            num.append(int(base[i]))
        elif base[i] == '.':
            result = str(num.pop())
        else:
            if len(num) >= 2:
                if base[i] == '+':
                    b = num.pop()
                    a = num.pop()
                    num.append(a+b)
                elif base[i] == '-':
                    b = num.pop()
                    a = num.pop()
                    num.append(a-b)
                elif base[i] == '*':
                    b = num.pop()
                    a = num.pop()
                    num.append(a*b)
                elif base[i] == '/':
                    b = num.pop()
                    a = num.pop()
                    num.append(a // b)
            else:
                result = 'error'
                break

    print('#{0} {1}'.format(tc+1, result))