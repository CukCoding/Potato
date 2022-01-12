expression = input().split('-')
num = []

for i in expression:
    cnt = 0
    tmp = i.split('+')
    for j in tmp:
        cnt += int(j)
    num.append(cnt)

n = num[0]

for i in range(1, len(num)):
    n -= num[i]

print(n)