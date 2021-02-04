way = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

def knight (sx, sy):
    q = [(sx, sy)]
    visted = [[0] * L for i in range(L)]
    visted[sx][sy] = 1
    count = 0

    if sx == fx and sy == fy :
        return count
    
    while q :
        temp = q
        q = []
        while temp :
            x, y = temp.pop()
            for dx, dy in way :
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < L and 0 <= ny < L :
                    if nx == fx and ny == fy :
                        count += 1
                        return count
                    
                    if not visted[nx][ny] :
                        q.append((nx, ny))
                        visted[nx][ny] = 1
        count += 1

T = int(input())
for test in range(T) :
    L = int(input())
    sx, sy = map(int, input().split())
    fx, fy = map(int, input().split())
    #result = 987654321
    visted = [[0] * L for i in range(L)]
    result = knight(sx, sy)
    print(result)