def dfs(v):
    visted[v] = 1
    for i in range(N):
        if graph[v][i] == 1 and visted[i] == 0:
            dfs(i)

N = int(input())
M = int(input())

graph = [[0] * N for _ in range(N)]
visted = [0 for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

dfs(0)
result = 0

for i in range(1,N):
    if visted[i] == 1:
        result += 1

print(result)