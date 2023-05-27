# https://level.goorm.io/exam/152114/%ED%98%84%EB%8C%80%EB%AA%A8%EB%B9%84%EC%8A%A4-%EC%98%88%EC%84%A0-dead-or-arrive/quiz/1

import sys
input = sys.stdin.readline

n = int(input())    # 차 대수 입력

speeds = {}
numbers = dict()

for i in range(n):
	v , w = map(int,input().split()) # 속도, 내구도 입력
	if v not in speeds:   # 처음 받는 속도이면
		speeds[v] = w # 내구도 추가
		numbers[v] = i+1    # 차번호 입력
	else:   # 이미 있는 속도이면 
		if speeds[v] <= w:    # 받은 내구도가 더 크면
			speeds[v] = w     # 내구도 갱신
			numbers[v] = i+1    # 차번호 입력/추가

answer = 0
for num in numbers.values():
	answer += num
	
print(answer)