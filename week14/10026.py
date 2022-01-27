from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())

s = [list(map(str, input())) for _ in range(N)]
c = [[0] * N for _ in range(N)]
q = deque()

def bfs(x, y):
    q.append([x, y])
    c[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if s[nx][ny] == s[x][y] and c[nx][ny] == 0:
                    q.append([nx, ny])
                    c[nx][ny] = 1

cnt = 0
for i in range(N):
    for j in range(N):
        if c[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')

for i in range(N):
    for j in range(N):
        if s[i][j] == 'R':
            s[i][j] = 'G'

c = [[0] * N for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if c[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)