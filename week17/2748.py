#2748 피보나치 수 2
n = int(input())        #n 입력

r = []                  #이미 계산한 피보나치를 저장하기 위한 리스트 r
num = 0                 #계산을 위한 변수 num

for i in range(n + 1):  
    if i == 0:          #입력한 숫자가 0 이면 num = 0
        num = 0
    elif i <= 2:        #입력한 숫자가 1, 2이면 num = 1
        num = 1
    else:               #그 이외의 수는 리스트 r의 맨 뒤의 두 숫자를 더한 것
        num = r[-1] + r[-2]
    r.append(num)       #계산한 num을 리스트 r에 추가

print(r[-1])            #리스트 r의 맨 뒤의 수를 출력