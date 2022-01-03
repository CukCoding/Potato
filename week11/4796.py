status = True
case = 1

while(status):
    L, P, V = map(int, input().split())
    day = 0
    
    if L == 0 and P == 0 and V == 0 :
        status = False
        break
    
    day = (V // P) * L 
    day += min((V % P), L)

    print("Case %d: %d" %(case, day)) 
    case += 1