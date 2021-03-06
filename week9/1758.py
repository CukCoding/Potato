import sys
N = int(input())
tip = []
for _ in range(N):
    tip.append(int(input()))
#팁을 많이 주는 사람이 앞으로 가야 더 많이 받을 수 있으므로
tip.sort(reverse=True)
result = 0
for i in range(N):
    t = tip[i] - i

    if t > 0:   #팁에서 순서-1 을 뺀 것이 양수일 때만 더함
        result += t

print(result)