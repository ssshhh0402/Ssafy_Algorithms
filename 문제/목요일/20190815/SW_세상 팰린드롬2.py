for tc in range(int(input())):
    in_word = list(input())
    result = 'Exist'
    for i in range(len(in_word)):
        if in_word[i] != in_word[-i - 1]:
            if i != len(in_word) + 1:
                result = 'Not Exist';

    print('#{0} {1}'.format(tc + 1, result))