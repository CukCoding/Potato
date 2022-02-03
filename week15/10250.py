def Hotel(H, W, N):
    cnt = 0
    for i in range(1, W + 1):
        for j in range(1, H + 1):
            cnt += 1
            if cnt == N :
                print(j * 100 + i)

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    Hotel(H,W,N)


