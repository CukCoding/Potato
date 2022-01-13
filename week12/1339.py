N = int(input())

word = []
for _ in range(N):
    word.append(list(map(lambda x: ord(x) - 65, input())))  #알파벳을 숫자로 바꾸어 인덱스로 활용

alpahbat = [0] * 26

for i in word:
    for j, char in enumerate(i[::-1]):
        alpahbat[char] += (10 ** j)

alpahbat.sort(reverse=True)

sum = 0
num = 9
for i in range(9):
    sum += num * alpahbat[i]
    num -= 1

print(sum)
