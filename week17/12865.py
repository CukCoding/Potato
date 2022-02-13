#물품의 수 N, 무게 W, 가치 V, 들 수 있는 무게 K

n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

dp  = [[0] * (k+1) for _ in range(n + 1)]

for i in range(1, n+1):             #가방에 담을 수 있는 물건의 개수를 1개부터 하나씩 늘림
    w, v = map(int, items[i-1])
    for j in range(1, k+1):
        if w <= j:  #담을 수 있는 무게보다 현재 물건이 작으면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)        #현재 물건을 넣었을 때와 넣지 않았을 때의 가치를 비교
        else:       #현재 물건이 담을 수 있는 무게보다 크면 해당 물건을 담지 않고 가방에 담을 수 있는 최고 가치를 저장
            dp[i][j] = dp[i-1][j]

print(dp[n][k])