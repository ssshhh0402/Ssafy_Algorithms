import sys
answer = []
tmp = 0
for tc in range(int(sys.stdin.readline())):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push_front':
        if len(answer) == 0:
            answer.append(int(order[1]))
        else:
            answer.append(0)
            for i in range(len(answer)-1, 0, -1):
                answer[i] = answer[i-1]

            answer[0] = int(order[1])
    elif order[0] == 'push_back':
        answer.append(int(order[1]))
    elif order[0] == 'pop_front':
        if len(answer) == 0:
            print(-1)
        else:
            print(answer.pop(0))
    elif order[0] == 'pop_back':
        if len(answer) == 0:
            print(-1)
        else:
            print(answer.pop(len(answer)-1))

    elif order[0] == 'size':
        print(len(answer))

    elif order[0] == 'empty':
        if len(answer) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(answer) == 0:
            print(-1)
        else:
            print(answer[0])
    elif order[0] == 'back':
        if len(answer) == 0:
            print(-1)
        else:
            print(answer[len(answer)-1])
