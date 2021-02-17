score = []  #점수받을 리스트 선언
for i in range(10): #10개의 점수 입력
    score.append(int(input()))

sum = 0     #점수의 합계
gap = []    #100과 sum의 차이를 리스트로 저장
flag = 987654321    #차이가 가장 작은 지점을 표시

for i in range(10):     
    sum += score[i]     #입력받은 점수를 sum에 더함
    gap.append(100 - sum)   #gap 리스트에 차이를 저장
    

for i in range(10):
    if abs(flag) >= abs(gap[i]):    #flag와 gap[i]의 절대값을 비교
        flag = gap[i]               #절대값이 더 작으면 flag 교체
print(100 - flag)                   #출력