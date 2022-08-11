# 시간과 분을 분으로 고쳐서 풀기

hour, min = map(int,input().split())

total = hour*60 + min
total -= 30

if total<0:
    hour = 23
    min = 60 + total
else:
    hour = total//60
    min = total%60

print(hour, min)
