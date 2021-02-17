num = int(input())
a = []
for i in range(0, num) :
    a.append(int(input()))

b = sorted(a)

for x in b :
    print(x)
