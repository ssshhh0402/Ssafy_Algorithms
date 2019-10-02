def find(a,b):  #a = 달, b = 금액
    global result,m_t,m_y
    if a == 12 and b < money[3]:
        result = min(result,b)
        return
    if b >= result:
        return
    elif b >= money[3]:
        result = min(result, money[3])
        return

    find(a+1, b + money[0] * base[a])
    find(a+1, b + money[1])
    if a + 3 <= 12:
        find(a+3, b+money[2])
    else:
        result = min(result,b+money[2])
        return


for tc in range(1, int(input())+1):
    money = list(map(int,input().split()))
    base = list(map(int,input().split()))
    result = 0xffffff
    m_t = False
    m_y = 0
    find(0,0)
    print("#{0} {1}".format(tc, result))
