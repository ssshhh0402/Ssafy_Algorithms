pos = True
count_a = []
for tc in range(int(input())):
    base = list(input())

    while len(base) != 0:
        a = base.pop()
        if a == ')':
            if '}' in count_a:
                pos = False
                break
            else:
                count_a.append(a)
        elif a == '}':
            count_a.append(a)
        elif a == '(':
            if len(count_a) != 0:
                if count_a[-1] == ')':
                    count_a.pop()
                else:
                    pos = False
                    break
            else:
                pos = False
                break
        elif a == '{':
            if len(count_a) != 0:
                if count_a[-1] == '}':
                    count_a.pop()

                else:
                    pos = False
                    break
            else:
                pos = False
                break
    # for i in range(len(base)):
    #     if base[i] == '(' or base[i] == '{':
    #         count_a.append(base[i])
    #     elif base[i] == ')':
    #         if len(count_a) != 0:
    #             if count_a[-1] == '(':
    #                 count_a.pop()
    #             else:
    #                 pos = False
    #                 break
    #         else:
    #             pos = False
    #             break
    #     elif base[i] == '}':
    #         if len(count_a) != 0:
    #             if count_a[-1] == '{':
    #                 count_a.pop()
    #             else:
    #                 pos = False
    #                 break
    #         else:
    #             pos = False
    #             break
    if pos and len(count_a) == 0:
        print('#{0} 1'.format(tc+1))
    else:
        print('#{0} 0'.format(tc+1))
