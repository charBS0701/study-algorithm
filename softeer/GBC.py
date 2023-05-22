# GBC
# https://softeer.ai/practice/info.do?idx=1&eid=584
# 0m 부터 100m까지 일정 구간들의 엘리베이터 속도를 검사
# n개의 엘리베이터 구간으로 나뉜다, 해당 구간의 제한속도 주어짐
# 구간의 총 합 100m, 구간별 길이, 제한속도

# 가장 제한속도를 크게 벗어난 값을 구한다

n, m = map(int, input().split())
limit = [0]*100
floor = 0
for i in range(n):
    section, limitSpeed = map(int, input().split())
    for i in range(section):
        limit[i+floor] = limitSpeed
    floor += section

floor = 0
overSpeed = 0
for i in range(m):
    section, testSpeed = map(int, input().split())
    for j in range(section):
        overSpeed = max(overSpeed, testSpeed - limit[j+floor])
    floor += section

print(overSpeed)
