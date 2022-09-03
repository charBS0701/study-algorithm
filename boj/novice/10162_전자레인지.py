t = int(input()) # 요리시간 입력
a = 5 * 60
b = 1 * 60
c = 10

count_a = 0
count_b = 0
count_c = 0

while t != 0:
    if t >= a:
        count_a += 1
        t -= a
        continue
    elif t >= b:
        count_b += 1
        t -= b
        continue
    elif t >= c:
        count_c += 1
        t -= c
    else:
        print(-1)
        break

if t == 0:
    print(count_a, count_b, count_c)