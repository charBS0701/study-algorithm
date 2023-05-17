# https://softeer.ai/practice/info.do?idx=1&eid=395
# 입력예제1
# 100 2
# 90 1
# 70 2
# 출력예제1
# 170
# W kg 까지 담을 수 있는 배낭
# 금속의 무게와 무게당 가격이 주어졌을 때, 배낭을 채우는 가장 비싼 가격?

bag, n = map(int,input().split()) # 담을 수 있는 배낭의 무게, 금속의 종류
nowBag = 0
money = 0 # 배낭에 담을 수 있는 가장 비싼 가격
materials = [0] * 10001 # 금속의 무게당 가격을 인덱스, 무게를 값으로 하는 리스트 초기화
for i in range(n):
    weight, value = map(int,input().split()) # 금속의 무게, 무게당 가격
    materials[value] += weight

for i in range(10000, 0, -1):
    if materials[i] != 0:
        if nowBag + materials[i] <= bag:    # 해당 가격의 금속을 다 담을 수 있으면
            nowBag += materials[i] # 가방에 담고
            money = money + i * materials[i] # 돈 계산
        else:   # 금속을 다 못 담으면
            money = money + i * (bag-nowBag) # 담을 수 있을 만큼만 값을 더한다다
            break

print(money)