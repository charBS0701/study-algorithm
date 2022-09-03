n = int(input())
for i in range(n):
    print(' '* (n-1-i) + '*'* (2*i+1))
for i in range(1,n):
    print(' '* i + '*'* (2*n-i*2-1))

## answer
# n=int(input()); max = n*2-1
# for i in range(-n+1,n):print(" "*abs(i)+"*"*(max-abs(i)*2))