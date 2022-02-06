s = list(input())   #입력받을 리스트 s 선언 후 입력
stack = []      #스택 구현을 위한 리스트 stack 선언
result = 0      #최종 출력을 위한 변수 result 선언
tmp = 1         #중간 연산을 위한 변수 tmp 선언

for i in range(len(s)): #s 길이 동안 반복 
    if s[i] == '(':     # 여는 괄호인 경우, 해당 원소를 stack에 추가
        stack.append(s[i])
        tmp *= 2        # ()은 2이므로, tmp에 2를 곱함
    elif s[i] == '[':
        stack.append(s[i])
        tmp *= 3        # []은 3이므로, tmp에 3을 곱함

    elif s[i] == ')':   # 닫는 괄호인 경우
        if not stack or stack[-1] == '[':   #stack이 비어있거나, stack의 top이 짝이 맞지 않는 경우
            result = 0  #result = 0
            break
        if s[i-1] == '(':   # 괄호의 짝이 맞는 경우, 중간 연산인 tmp를 result에 더함
            result += tmp
        stack.pop()         # 여는 괄호 stack에서 제거
        tmp //= 2           # tmp의 값을 2나 3으로 나누어 원래의 값으로 만들어줌
    else:
        if not stack or stack[-1] == '(':
            result = 0
            break
        if s[i-1] == '[':
            result += tmp
        stack.pop()
        tmp //= 3
    
if stack:       # 위 과정을 마친 뒤에도 stack에 원소가 남아있다면, 짝이 맞지 않은 것이므로 0 출력
    print(0)
else:           # 결과값 출력
    print(result)