#https://softeer.ai/practice/info.do?idx=1&eid=624
# 입력예제
# 2
# 1 2
# 9881 10724
# 출력 예제
# 5
# 11

import sys

t = int(input())

lamp = { 
' ':[0,0,0,0,0,0,0], 
'0': [1,1,1,1,1,1,0], 
'1': [0,1,1,0,0,0,0], 
'2': [1,1,0,1,1,0,1], 
'3':[1,1,1,1,0,0,1], 
'4':[0,1,1,0,0,1,1], 
'5':[1,0,1,1,0,1,1],
'6': [1,0,1,1,1,1,1], 
'7':[1,1,1,0,0,1,0], 
'8':[1,1,1,1,1,1,1], 
'9':[1,1,1,1,0,1,1]}

# 테스트 케이스 t번 반복
for _ in range(t):
    a, b = input().split()
    count = 0
    
    # 불꺼진 수 처리
    a = a.rjust(5, " ")
    # b = b.rjust(5, " ")
    # a = (5-len(a))*" " + a
    b = (5-len(b))*" " + b
    
    for i in range(5):
        for x in range(7):
            if lamp[a[i]][x] != lamp[b[i]][x]:
                count += 1
    
    print(count)