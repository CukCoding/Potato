#11052 카드 구매하기
N = int(input())        #구입하려는 카드의 수
price = [0]             #카드팩의 가격 
price += list(map(int, input().split()))
d = [0] * (N+1)         #N장을 구매할 때 최대가격

d[1] = price[1]         #1장을 구매할 때는 pirce[1]과 동일
d[2] = max(price[1] * 2 , price[2]) #2장을 구매할 때는 1장짜리 2개 또는 2장짜리 하나 중 더 큰 가격

for i in range(3, N+1):
    d[i] = price[i]     #N장짜리 카드팩의 가격을 저장
    for j in range(1, i//2 + 1):    #저장된 값과 (i-j)+j 를 비교하여 더 큰값 저장
        d[i] = max(d[i], d[i-j]+d[j])   

print(d[N])