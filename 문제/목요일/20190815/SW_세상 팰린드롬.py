for i in range(int(input())):
    word_a = list(input())
    result= 'Exist'
    if '?' not in word_a:
        if word_a != word_a[::-1]:
            result = 'Not exist'
    else:
        for h in range(len(word_a)//2):
            if word_a[h] != word_a[-1-h]:
                result = 'Not exist'
                break
            else:
                if word_a[h] == '?' and word_a[-1-h] == '?':
                    continue
    print('#{0} {1}'.format(i+1, result))
        # ? 위치 찾아서
        # ? 위치 아스키 코드 사용 포문으로 모든 알파벳 다 뒤져 가면서
        # pelindrom 되면 끝
        # 아닌거 같다
        # 흠
        #
