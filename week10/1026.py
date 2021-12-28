N = int(input())        #배열의 길이 N 입력

#리스트 A, B 입력
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

S = 0   #S 초기화 

for i in range(N):
    A = list_a.pop(list_a.index(min(list_a)))   #list_a의 최소값을 pop하여 A에 저장
    B = list_b.pop(list_b.index(max(list_b)))   #list_b의 최대값을 pop하여 B에 저장
    S += A * B

print(S)