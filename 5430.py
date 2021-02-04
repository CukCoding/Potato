T = int(input())

for _ in range(T) :
    F = list(input())
    n = int(input())
    de = input()[1:-1].split(',')

    r_count = 0
    d_count = 0
    error = False

    for i in F :
        if i == 'R' :
            r_count += 1
        else :
            try:
                if r_count % 2 == 0 :
                    d_count += 1
                else :
                    de.pop()
            except:
                error = True
                break
        
    if error or d_count > n :
        print("error")
        continue
    
    if r_count % 2 == 0 :
        answer = de[d_count:]
    else:
        answer = list(reversed(de[d_count:]))
    
    print("[", end='')
    for i in range(len(answer)) :
        if i == len(answer) - 1 :
            print(answer[i], end='')
        else :
            print("%s," %answer[i], end='')
    print("]")