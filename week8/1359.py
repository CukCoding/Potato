def Combination(n, r):  #조합 함수
    p = 1
    c = 1
    while r > 0 :
        c *= n
        p *= r
        n -= 1
        r -= 1
    return c/p

N, M, K = map(int, input().split())
p = Combination(N, M)   #N개 중 M개를 뽑는 확률
result = 0

while K <= M:   
    if N - M < M - K :  #조합이 성립하지 않을 때
        K += 1
        continue
    c = Combination(M, K) * Combination(N-M, M - K) #내가 뽑은 M개 중 K개가 겹치고 X 내가 뽑지 않은 것 중 겹치지 않는 것

    result += c/p   #K가 M과 같아질 때까지의 값을 더함 
    K += 1

print(result)