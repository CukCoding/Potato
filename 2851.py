score = []
for i in range(10):
    score.append(int(input()))

sum = 0
gap = []
flag = 987654321
for i in range(10):
    sum += score[i]
    gap.append(100 - sum)
    

for i in range(10):
    if abs(flag) >= abs(gap[i]):
        flag = gap[i]
print(100 - flag)