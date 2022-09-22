array = [] # 수열 하나 생성
n = int(input()) # 수열의 크기 입력
for _ in range(n): # 수열 입력
    array.append(int(input()))

# 내림차순 정력
array.sort(reverse=True)
# array = sorted(array, reverse=True)

for x in array:
    print(x, end=' ')