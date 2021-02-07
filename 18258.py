from collections import deque

import sys
input = lambda : sys.stdin.readline().strip()
N = int(input())
de = deque()

for i in range(N) :
    a = input().split()

    if a[0] == 'push' :
        de.append(a[1])
    elif a[0] == 'pop' :
        if len(de) >= 1 :
            print(de.popleft())
        else :
            print(-1)
    elif a[0] == 'size' :
        print(len(de))
    elif a[0] == 'empty' :
        if len(de) == 0 :
            print(1)
        else :
            print(0)
    elif a[0] == 'front' :
        if len(de) == 0 :
            print(-1)
        else :
            print(de[0])
    elif a[0] == 'back' :
        if len(de) == 0 :
            print(-1)
        else : 
            print(de[-1])