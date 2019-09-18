import copy
N, M = map(int, input().split())
base = [list(map(int, input().split())) for _ in range(N)]
# 1 번일 경우, 움직이고, 경로 스택에 다 저장해 놓고
# 비교해봤을 때 더 큰아이를 작은아이한테 deep copy
# 비교 끝났을 때 가장 큰 아이를 1로ㅇㅇ

