T = int(input())    #테스트 케이스 횟수

for _ in range(T):
    N, M = map(int, input().split())    # M: 문서의 개수, M = 인쇄횟수가 궁금한 문서의 위치
    index = []  # M 원소를 저장하기 위한 리스트 선언
    for i in range(N):
        index.append(i)
    index[M] = -1   # M번째 원소 표시
    importance = list(map(int, input().split()))    #중요도 저장
    
    cnt = 1     #출력되는 순서 카운팅
    x = 0       #while문 안에서 인덱스 역할
    while importance:
        out = max(importance)   #중요도 리스트 내에서 최댓값 저장
        if importance[x] < out: #중요도가 가장 크지 않으면 맨 뒤로 보냄
            importance.append(importance.pop(0))
            index.append(index.pop(0))
        
        elif importance[x] == out:  #가장 큰 중요도 일때
            importance.pop(0)       #해당 중요도 제거
            if index[x] == -1:      #만약 M번째 문서라면 해당 문서 제거 후 cnt 출력 후 반복문 종료
                index.pop(0)        
                print(cnt)          
                break
            index.pop(0)
            cnt += 1
        
        