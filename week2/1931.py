num = int(input())
timetable = []
count = int(1)

for i in range(num): 
    start, finish = map(int, input().split())
    timetable.append([start, finish])

s = sorted(timetable, key = lambda x : (x[1],x[0]))

data = s[0][1]
for i in range(1, num):
    if data <= s[i][0]:
        count += 1
        data = s[i][1]

print(count)