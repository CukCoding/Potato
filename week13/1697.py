from collections import deque

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(visted[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not visted[nx]:
                visted[nx] = visted[x] + 1
                q.append(nx)

MAX = 100000
visted = [0] * (MAX + 1)
N, K = map(int, input().split())

bfs()