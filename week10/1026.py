N = int(input())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

S = 0
for i in range(N):
    A = list_a.pop(list_a.index(min(list_a)))
    B = list_b.pop(list_b.index(max(list_b)))
    S += A * B

print(S)