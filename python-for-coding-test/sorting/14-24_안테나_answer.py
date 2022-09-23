n = int(input()) # 집의 수 입력
houses = list(map(int,input().split()))
houses.sort()

# 중간값(median)을 출력
print(houses[(n-1) // 2])