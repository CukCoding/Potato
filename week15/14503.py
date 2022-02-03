import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(x, y, d):
    global cnt
    if arr[x][y] == 0:  #청소할 수 있으면 2로 바꾸고 cnt 1 증가
        arr[x][y] = 2
        cnt += 1
    
    for _ in range(4):
        nd = (d + 3) % 4    # << 이게 왼쪽 방향
        nx = x + dx[nd]
        ny = y + dy[nd]
        if arr[nx][ny] == 0:    #왼쪽 방향이 0 이면 clean함수에 다음 좌표 및 방향 입력
            clean(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4    #뒤로 이동 가능한지 확인
    nx = x + dx[nd]
    ny = y + dy[nd] 
    if arr[nx][ny] == 1:    #뒤가 벽이면 종료
        return
    clean(nx, ny, d)    #아니면 다음 좌표, 방향 입력. 이때 방향은 유지한 채로 뒤로 이동했기 떄문에 d 입력
 
N, M = map(int, input().split())
rx, ry, d = map(int, input().split())

cnt = 0

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

clean(rx, ry, d)

print(cnt)