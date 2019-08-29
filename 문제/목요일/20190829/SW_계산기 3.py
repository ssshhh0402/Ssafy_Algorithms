for tc in range(10):
    l = int(input())
    base = list(input())
    val = {'*': 2, '+': 1, '(': 3}
    cal = []
    p_fix = []
    answer = []
    for i in range(l):
        if base[i].isdigit():
            p_fix.append(base[i])
        else:
            if base[i] == ')':
                while cal[-1] == '(':
                    p_fix.append(cal.pop())
                a = cal.pop()
                if a != '(':
                    p_fix.append(a)
            else:
                if len(cal) == 0:
                    cal.append(base[i])
                elif val[base[i]] > val[cal[-1]]:
                    a = base[i]
                    if a != '(':
                        p_fix.append(a)

                else:
                    while True:
                        a = cal.pop()
                        if a != '(':
                            p_fix.append(a)
                        if len(cal) == 0 or val[base[i]] > val[cal[-1]]:
                            break
                    cal.append(base[i])

    if not cal:
        while cal:
            p_fix.append(cal.pop())
    print(p_fix)
    # for idx in p_fix:
    #     if idx.isdigit():
    #         answer.append(idx)
    #     else:
    #         if idx == '+':
    #             a = answer.pop()
    #             b = answer.pop()
    #             answer.append(a+b)
    #         elif idx == '*':
    #             a = answer.pop()
    #             b = answer.pop()
    #             answer.append(a*b)
    #
    # print('#{0} {1}'.format(tc+1, answer.pop()))
