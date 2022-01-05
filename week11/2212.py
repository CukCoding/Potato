N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
distance = []
sensor.sort()

if N <= K:
    print(0)
    quit()

for i in range(1,N):
    distance.append(sensor[i]-sensor[i-1])


distance.sort(reverse=True)

for i in range(K-1):
    distance.pop(0)

print(sum(distance))