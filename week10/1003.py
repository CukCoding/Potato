""" 
zero = 0
one = 0

def fib(n):
    global zero
    global one 
    if n == 0:
        zero = zero + 1
        return 0
    elif n == 1:
        one += 1
        return 1
    else :
        return (fib(n-1) + fib(n-2))


t = int(input())

for i in range(t):
    zero = 0
    one = 0

    n = int(input())
    fib(n)

    print(zero, one) 
"""

#풀었는데 시간초과

zero = [1,0]
one = [0,1]

def fib(n):
    if n > 1 :
        for i in range(n-1): 
            zero.append(zero[-2]+zero[-1])
            one.append(one[-2]+one[-1])

    print(zero[n], one[n])

T = int(input())

for i in range(T):
    zero = [1,0]
    one = [0,1]
    fib(int(input()))