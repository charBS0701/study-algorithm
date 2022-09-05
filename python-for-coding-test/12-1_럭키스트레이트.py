# 점수가 특정 조건을 만족할 때만 사용가능
# 점수 N이 자릿수를 기준으로 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황
# 할수있는지

n = input()
left = 0
right = 0

for i in range(len(n)//2):
    left += int(n[i])
    right += int(n[-i-1])

if left == right :
    print('LUCKY')
else:
    print('READY')
