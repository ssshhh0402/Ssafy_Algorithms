# def backtrack(k,x,y,size):
#     global ans
#     if k >= ans:
#         return True
#     r, c = getNext(x, y)
#     if r == 10:
#         ans = min(ans, k)
#         return True
#     ret = False
#     for i in range(5, 0, -1):
#         if paper[i] and isPossible[r,c,i):
#             setValue(r, c, i ,0)
#
#
#
#
# paper = [0,5,5,5,5,5]
# arr = [list(map(int, input().split())) for _ in range(10)]
# ans = 101
# if backtrack(1,0,1):