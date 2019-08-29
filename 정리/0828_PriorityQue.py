# from queue import PriorityQueue
#
#
# arr = [(3, 4), (3, 5), (8, 9), (1, 4), (2, 6),(3,7)]
# PQ = PriorityQueue()
#
#
# for val in arr:
#     PQ.put(val)
#
#
# while not PQ.empty():
#     print(PQ.get())

from heapq import heappush, heappop

Q = []
arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

for val in arr:
    heappush(Q, val)

while len(Q) > 0:
    print(heappop(Q))
