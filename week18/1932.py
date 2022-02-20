#1932 정수 삼각형

N = int(input())    #삼각형의 크기 N 입력
tri = []
for i in range(N):
    tri.append(list(map(int,input().split())))

width = 2

for i in range(1, N):
    for j in range(width):
        if j == 0 :         #만약 왼쪽 가장 바깥쪽 숫자라면 바로 위 오른쪽 숫자와 더함
            tri[i][j] = tri[i-1][j] + tri[i][j]
        elif j == i :       #만약 오른쪽 가장 바깥쪽 숫자라면 바로 위 왼쪽 숫자와 더함
            tri[i][j] = tri[i-1][j-1] + tri[i][j]
        else :              #만약 가운데 숫자라면 바로 위의 양 수를 비교하여 더 큰 값과 더함
            tri[i][j] = max(tri[i-1][j], tri[i-1][j-1]) + tri[i][j]
    
    width += 1

print(max(tri[N-1]))