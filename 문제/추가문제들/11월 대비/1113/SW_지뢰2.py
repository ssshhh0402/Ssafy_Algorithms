from collections import deque


def Group(a):
    global visited              # count = 그룹에 속한 원소 갯수 , group_count = 그룹 갯수
    count = 0
    group_count = 0
    for item in a:
        if not visited[item[0]][item[1]]:
            group_count += 1
            count += 1
            visited[item[0]][item[1]] = 1
            stck = deque([(item[0], item[1])])
            while stck:
                i_x, i_y = stck.popleft()
                for dx_2, dy_2 in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    x_2, y_2 = i_x + dx_2, i_y + dy_2
                    if 0 <= x_2 < N and 0 <= y_2 < N and not visited[x_2][y_2]:
                        if base[x_2][y_2] == 0:
                            visited[x_2][y_2] = 1
                            stck.append((x_2,y_2))
                            count += 1
                        elif 0 < base[x_2][y_2] < 9:
                            visited[x_2][y_2] = 1
                            count += 1
    return count, group_count


for tc in range(1, int(input())+1):                                                           # 연결된 0끼리 묶어서 그룹 만들고
    N = int(input())                                                                       #연결된 0그룹 갯수 + 나머지 하나짜리들 갯수 계산
    base = [list(input()) for _ in range(N)]
    visited = [[0 for _ in range(N)]for _ in range(N)]
    young = []
    star_c = 0
    for i in range(N):
        for j in range(N):
            if base[i][j] == '.':
                cnt = 0
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    x, y = i+dx, j+dy
                    if 0 <= x < N and 0 <= y < N:
                        if base[x][y] == '*':
                            cnt += 1
                base[i][j] = cnt
                if not cnt:
                    young.append((i, j))
            elif base[i][j] == '*':
                visited[i][j] = 1
                star_c += 1
    group, group_c = Group(young)                   # group : 그룹에 속한 원소 갯수 , group_c = 그룹 갯수
    sole = N * N - group - star_c   
    print("#{0} {1}".format(tc, group_c + sole))
