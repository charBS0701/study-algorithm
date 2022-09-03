hour, min, sec = map(int,input().split())
cook_time = int(input())

sec = (hour * 60 * 60) + (min * 60) + sec + cook_time

hour = sec // 3600 if (sec // 3600) < 24 else (sec // 3600) - 24
sec = sec % 3600 
min = sec // 60
sec = sec % 60

print(hour, min, sec)