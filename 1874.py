import sys

n = int(input())
a = []
b = []
op = []
for i in range(0, n) :
    a.append(int(input()))

top = int(0)
index = int(1)

for i in range(0, n) :
    while index <= a[i] :
        b.append(index)
      
        index += 1
        op.append('+')
        top += 1
       
    if b[top - 1] == a[i] :
        op.append('-')
        del b[top -1]
        top -= 1
    else :
        print("NO")
        exit()
    
for i in op :
    print(i)
