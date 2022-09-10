# 2중 반복문 구조를 이용하는 답안 예시

n,m = map(int, input().split()) # 행열 수 입력

result = 0
for i in range(n):
    data = list(map(int,input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001 # 입력 범위보다 큰 값으로 설정
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력        
