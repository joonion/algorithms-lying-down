from heapq import heappop, heappush

def knapsack1(n, W, maxprofit, totprofit, heap):
    return 0
    
n, W = map(int, input().split())
heap = []
for _ in range(n):
    w, p = map(int, input().split())
    heappush(heap, (-p/w, w, p))
maxprofit = knapsack1(n, W, heap)
print(maxprofit)

