M = input() #정인이가 보낸 메시지
N = len(M)
C = N
R = 1
for i in range(1,N): 
    s = N / i
    if N % i == 0:
        if s >= i:
            R = i

C = N//R


decrypt = [['' for _ in range(C)] for _ in range(R)]
cnt = 0
for j in range(C):
    for i in range(R):
        decrypt[i][j] = M[cnt]
        cnt += 1

for i in range(R):
    for j in range(C):
        print(decrypt[i][j], end='')