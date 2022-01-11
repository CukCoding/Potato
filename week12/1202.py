import heapq
import sys

N, K = map(int, sys.stdin.readline().split())

jewel = []
bag = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    heapq.heappush(jewel, [M, V])

for _ in range(K):
    heapq.heappush(bag, int(sys.stdin.readline()))

result = 0
available = []

for _ in range(K):
    capacity = heapq.heappop(bag)

    while jewel and capacity >= jewel[0][0]:
        heapq.heappush(available, -heapq.heappop(jewel)[1])

    if available:
            result -= heapq.heappop(available)
    elif not jewel:
            break

print(result)