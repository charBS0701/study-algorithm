hour, min = map(int,input().split())
cook_time = int(input())

min = hour * 60 + min + cook_time
hour = min // 60 if min // 60 < 24 else min // 60 - 24
min = min % 60

print(hour, min)