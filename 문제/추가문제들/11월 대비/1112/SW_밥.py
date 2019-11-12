from collections import deque


def door_1(a):              # 1번째 문으로 이동하는 후 다 빠져나가는 시간 계산
    if not a:
        return 0            # 거리 계산하고
    else:
        dist = deque([])
        for person in a:
            dist.append(abs(doors[0][0] - person[0]) + abs(doors[0][1] - person[1]))
        i_time = 0
        count = 0
        stair = deque([])
        wait = deque([])
        while dist or stair:
            if dist:                                                # 이동 중인 사람 있을 때
                for _ in range(len(dist)):                                      
                    x = dist.popleft()                               #  뽑아 와서
                    if not x:                                         # 0 이면
                        if len(stair) < 3:                                 # 계단 사람 수 확인
                            stair.append(doors_value[0])                    # 3명 아래면 사람 추가하고 count + 1
                            count += 1
                        else:                                           # 3명이면 대기열 추가
                            wait.append(doors_value[0])
                    else:
                        x -= 1                                      #0 이 아니면
                        dist.append(x)                              # 거리 -1하고 다시 이동 배열
            if stair:                                               # 계단 사람 있으면
                for _ in range(len(stair)): 
                    y = stair.popleft()                              # 한명씩 뽑아와서
                    y -= 1                                            # -1 하고
                    if not y:                                           # 0이면(다내려갔으면)
                        if not wait:                                       # 기다리는 사람 확인
                            count -= 1                                         # 기다리는 사람 없으면 그냥 인원수 -1
                        else:
                            stair.append(wait.popleft())                           # 있으면 기다리는 사람 계단 ㄱㄱ
                    else:
                        stair.append(y)                                 # 0이 아니면 다시 계단
            i_time += 1                                         # 여기까지가 한텀

        return i_time+1


def door_2(a):              # 2번째 문으로 이동 후 다 빠져나가는 시간 계산
    if not a:
        return 0
    else:
        dist_two = deque([])
        for person in a:
            dist_two.append(abs(doors[1][0] - person[0]) + abs(doors[1][1] - person[1]))
        im_time = 0
        count = 0
        stair_two = deque([])
        wait_two = deque([])
        while dist_two or stair_two:
            if dist_two:  # 이동 중인 사람 있을 때
                for _ in range(len(dist_two)):
                    x = dist_two.popleft()  # 뽑아 와서
                    if not x:  # 0 이면
                        if len(stair_two) < 3:  # 계단 사람 수 확인
                            stair_two.append(doors_value[1])  # 3명 아래면 사람 추가하고 count + 1
                            count += 1
                        else:  # 3명이면 대기열 추가
                            wait_two.append(doors_value[1])
                    else:
                        x -= 1  # 0 이 아니면
                        dist_two.append(x)  # 거리 -1하고 다시 이동 배열
            if stair_two:  # 계단 사람 있으면
                for _ in range(len(stair_two)):
                    y = stair_two.popleft()  # 한명씩 뽑아와서
                    y -= 1  # -1 하고
                    if not y:  # 0이면(다내려갔으면)
                        if not wait_two:  # 기다리는 사람 확인
                            count -= 1  # 기다리는 사람 없으면 그냥 인원수 -1
                        else:
                            stair_two.append(wait_two.popleft())  # 있으면 기다리는 사람 계단 ㄱㄱ
                    else:
                        stair_two.append(y)  # 0이 아니면 다시 계단
            im_time += 1  # 여기까지가 한텀
        return im_time+1


def find(a):     # I_one = 1번 문으로 나가는 사람들, I_two = 2번 문으로 나가는 사람들
    global result
    for set in range(0, 1 << (M+1)):
        l_one, l_two = [], []
        for i in range(M):
            if set & (1 << i):
                l_one.append(a[i])
            else:
                l_two.append(a[i])
        time = max(door_1(l_one), door_2(l_two))
        result = min(result, time)


for tc in range(1, int(input())+1):
    N = int(input())
    base = [list(map(int,input().split())) for _ in range(N)]
    people = []
    doors = []
    doors_value = []
    result = 0xffffff
    for i in range(N):
        for j in range(N):
            if base[i][j] > 0:
                if base[i][j] == 1:
                    people.append((i,j))
                else:
                    doors.append((i,j))
                    doors_value.append(base[i][j])
    M = len(people)
    find(people)
    print("#{0} {1}".format(tc, result))
