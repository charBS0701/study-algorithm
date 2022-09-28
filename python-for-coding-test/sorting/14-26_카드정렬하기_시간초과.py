n = int(input()) # 숫자 카드 묶음의 수 입력
# 숫자 카드 묶음 크기 입력
data = []
for i in range(n):
    data.append(int(input()))

sum = 0

# 시간복잡도 : (n-1) * nlogn = n**2logn
# n = 100,000, 10,000,000,000 10억. 시간제한:2초, 2억
while True:
    data.sort()
    if len(data) == 1 :
        if sum == 0:
            sum += data[0]
            break
        break
    data.append(data[0]+data[1])
    sum += data[-1]
    data.pop(0)
    data.pop(0)

print(sum)