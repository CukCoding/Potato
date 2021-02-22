import sys 
num, M = map(int, input().split())
Tree = list(map(int, input().split()))

start = 1
end = max(Tree)

while start <= end:
    mid = (start + end) // 2
    cut = 0
    for i in Tree:
        if i > mid:
            cut += i-mid
    
    if cut >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end) 

#시간초과