def cal(n):
    n = n//10
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 2 * cal(10*(n-1)) + 1
        else:
            return 2 * cal(10*(n-1)) - 1




for tc in range(int(input())):
    #  N 입력받고
    # 10의 배수라는건 1,2,3 처럼 사용하라는거같은데..
    print('#{0} {1}'.format(tc+1, cal(int(input()))))
