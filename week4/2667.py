def bfs (house, i, j, N, visted) :
    if house[i][j] == 0:
        visted.append([i, j])
        return [0, visted]
    
    block = []
    queue = [[i, j]]

    while queue :
        [i, j] = queue.pop(0)
        block.append([i, j])
        visted.append([i, j])

        if house[i][j] == 1:
            if i < N-1 and house[i+1][j] == 1 and [i+1, j] not in block and [i+1, j] not in queue:
                queue.append([i+1, j])
            
            if j < N-1 and house[i][j+1] == 1 and [i, j+1] not in block and [i, j+1] not in queue:
                queue.append([i, j+1])
            
            if j > 0 and house[i][j-1] == 1 and [i, j-1] not in block and [i, j-1] not in queue:
                queue.append([i, j-1])
            
            if i > 0 and house[i-1][j] == 1 and [i-1, j] not in block and [i-1, j] not in queue:
                queue.append([i-1, j])
            
    return [len(block), visted]


N = int(input())

house = []
visted = []
result = []

for _ in range(N):
    house.append(list(map(int, str(input()))))

for i in range(N):
    for j in range(N):
        if [i, j] not in visted:
            [size, visted] = bfs(house, i, j, N, visted)
            if size != 0:
                result.append(size)

print(len(result))
result.sort()
for i in result:
    print(i)