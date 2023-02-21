n = int(input())
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance =  ((x1-x2)**2 +(y1-y2)**2)**(1/2)
    if (distance == r1+r2) or (abs(r1-r2) == distance): # 외접 또는 내접
        answer = 1
    elif distance == 0 and r1==r2: # 동심원이고 반지름이 같을 때
        answer = -1
    elif (r1 + r2 > distance) and (abs(r1-r2) < distance): # 다른 두점에서 만날 때
        answer = 2
    else:
        answer = 0
    print(answer)
