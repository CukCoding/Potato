count = int(input())

for i in range(0, count) : 
    score = []
    a = 0

    score = list(map(int, input().split(' ')))
    average = sum(score[1:])/score[0]

    for k in score[1:] :
        if average < k :
            a += 1
    print(format(a/score[0]*100,".3f"),end='')
    print("%")

    