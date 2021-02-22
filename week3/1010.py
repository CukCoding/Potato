def factorial(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    bridge = factorial(M) // (factorial(M-N)*factorial(N))
    print(bridge)