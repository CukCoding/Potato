import sys
N = int(input())    #입력받을 단어 개수
result = 0  #그룹 단어 개수

for _ in range(N):
    word = input()
    error = 0   #문자가 떨어져 있는 경우
    for i in range(len(word)-1):    #단어길이 - 1 까지 진행
        if word[i] != word[i+1]:    
            new_word = word[i+1:]
            if new_word.count(word[i]) > 0:
                error += 1
    if error == 0:
        result += 1

print(result)

