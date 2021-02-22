game = [list(map(int, input().split())) for _ in range(9)]  

zeros = []
for i in range(9):
    for j in range(9):
        if game[i][j] == 0:
            zeros.append((i, j))


def is_checking (i, j) :
    checking = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for k in range(9):
        if game[i][k] in checking:
            checking.remove(game[i][k])
        if game[k][j] in checking:
            checking.remove(game[k][j])

    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if game[p][q] in checking:
                checking.remove(game[p][q])

    return checking

flag = False

def dfs(x):
    global flag

    if flag: 
        return
    

    if x == len(zeros):
        for row in game:
            print(*row)
        flag = True 
        return

    else:
        (i, j) = zeros[x]
        checking = is_checking(i, j)

        for num in checking:
            game[i][j] = num 
            dfs(x+1)
            game[i][j] = 0

dfs(0)