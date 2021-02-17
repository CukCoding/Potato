n,c = map(int, (input().split()))
home = []

for i in range(n): 
    home.append(int(input()))
home.sort()

min_gap = 1
max_gap = home[-1] - home[0]
result_gap = 0

while min_gap <= max_gap : 
    gap = (min_gap + max_gap) // 2
    value = home[0]
    count = 1
    for i in range(1,len(home)):
        if home[i] >= value + gap:
            value = home[i]
            count += 1
    if count >= c:
        min_gap = gap + 1
        result_gap = gap
    else :
        max_gap = gap - 1

print(result_gap)