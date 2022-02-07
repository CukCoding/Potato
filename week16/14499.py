def move(d):    #주사위 이동 시 옆면은 변하지 않음
    if d == 1:  #동
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif d == 2:    #서
        dice[3], dice[0], dice[2], dice[5] = dice[0], dice[2], dice[5], dice[3]
    elif d == 3:    #북
        dice[1], dice[5], dice[4], dice[0] = dice[0], dice[1], dice[5], dice[4]
    elif d == 4:    #남
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]

N, M, x, y, K = map(int, input().split())
s = []
for i in range(N):
    s.append(list(map(int, input().split())))

dice = [0] * 6       #위 / 북 / 동 / 서 / 남 / 바닥 

dice_move = [[0, 0], [0,1], [0, -1], [-1, 0], [1, 0] ]      #동, 서, 남, 북

for order in map(int, input().split()):
    dx, dy = dice_move[order]
    dx += x
    dy += y
    if 0 <= dx < N and 0 <= dy < M:
        move(order)
        if not s[dx][dy]:
            s[dx][dy] = dice[5]
        else:
            s[dx][dy], dice[5] = 0, s[dx][dy]
        print(dice[0])
        x, y = dx, dy


# https://www.acmicpc.net/board/view/72562