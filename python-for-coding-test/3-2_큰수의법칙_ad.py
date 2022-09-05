# m의 수가 크다면 시간초과가 나올 수도 있다.
# 수학적 아이디어로 더 효율적으로 문제를 해결해보자

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번쨰로 큰 수 더하기

print(result) # 최종 답안 출력
