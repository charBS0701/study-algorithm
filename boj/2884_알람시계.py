## 2023년 풀이
h, m = map(int, input().split(' '))

if m<45 and h==0:
    h=24
total = h*60 + m

total -= 45
print(total//60, total%60)

## 2021년 풀이
# h, m = map(int, input().split())
# if 45 <= m:
#     print(h, m-45)
# elif h != 0:
#     print(h-1, m+60-45)
# else:
#     print(23, m+60-45) 