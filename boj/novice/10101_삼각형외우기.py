a = int(input())
b = int(input())
c = int(input())

if a+b+c == 180:
    if a == b and a == c:
        print('Equilateral')
    elif a == b or a == c or b == c:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')