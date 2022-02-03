from collections import deque

q = deque()
result = []
N, K = map(int, input().split())

for i in range(1, N + 1):
    q.append(i)

while q :
    for i in range(K - 1):
        q.append(q.popleft())
    result.append(q.popleft())

print("<", end='')
for i in range(len(result) - 1):
    print("%d, " %result[i] , end='')
print(result[-1], end='')
print(">")