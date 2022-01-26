from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
M = int(input())
s = [[] for _ in range(N + 1)]
result = [0 for _ in range(N + 1)]

def bfs(key):
    q = deque()
    q.append(key)
    visit = [0 for _ in range(N + 1)]
    visit[key] = 1
    while q:
        temp = q.popleft()
        for i in s[temp]:
            if visit[i] == 0:
                visit[i] = 1
                result[i] = result[temp] + 1
                q.append(i)

for i in range(M):
    x, y = map(int, input().split())
    s[x].append(y)
    s[y].append(x)

bfs(a)
if result[b] != 0 :
    print(result[b])
else:
    print(-1)

