#11726 2xn 타일링
# 2 * N 일떄 2*1 블럭으로 채울 수 있는 경우의 수를 10007로 나눈 나머지 출력
# N = 1 일때는 1, N = 2 일때는 2, N = 3 일때는 3, N = 4 일때는 5, N = 5 일때는 8
# 가장 직전 두개의 합이 된다

n = int(input())
r = [0, 1, 2]
for i in range(3, n+1):
    r.append(r[i-1] + r[i-2])

print(r[n] % 10007)