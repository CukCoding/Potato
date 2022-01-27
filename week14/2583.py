M, N, K = map(int,input().split())
s = [[0] * N for _ in range(M)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = []

for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())

    for i in range(ly, ry):
        for j in range(lx, rx):
            s[i][j] = 1


for i in range(M):
    for j in range(N):
        if s[i][j] == 0:
            count = 1
            s[i][j] = 1
            queue = [[i, j]]
            while queue:
                x, y = queue[0][0], queue[0][1]
                del queue[0]
                for k in range(4):
                    x1 = x + dx[k]
                    y1 = y + dy[k]
                    if 0 <= x1 < M and 0 <= y1 < N and s[x1][y1] == 0:
                        s[x1][y1] = 1
                        count += 1
                        queue.append([x1, y1])
            result.append(count)

print(len(result))
result.sort()
for i in result:
    print(i, end=' ')