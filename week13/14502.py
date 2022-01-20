import sys
import copy
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int,input().split())

lab = []
for i in range(N):
    lab.append(list(map(int,input().split())))


max_result = 0
q = deque()


def bfs() :
    global max_result
    save = copy.deepcopy(lab)
    for i in range(N):
        for j in range(M):
            if save[i][j] == 2:
                q.append([i, j])
    
  

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if save[nx][ny] == 0:
                    save[nx][ny] = 2
                    q.append([nx, ny])
    
    result = 0
    
    for i in save:
        result += i.count(0)

    max_result = max(max_result, result)

def wall(cnt) :
    
    if cnt == 3:
        bfs()
        return 
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(cnt+1)
                lab[i][j] = 0


wall(0)
print(max_result)