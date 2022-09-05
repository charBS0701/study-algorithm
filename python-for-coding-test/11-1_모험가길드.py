# N명의 모험가를 대상으로 '공포도' 측정
# '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어짐
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록
# 최대 몇 개의 모험가 그룹을 만들 수 있는지
# N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하라

n = int(input()) # 모험가 수 입력
fears = list(map(int,input().split())) # 공포도 입력

fears = sorted(fears, reverse=True) # 공포도가 큰순으로 정렬


groups = list()
# 리스트형 2차 배열
for i in range(n):
    groups.append([])

count = 0 # 확인하고있는 모험가의 인덱스
result = 0 # 결과값
while True:
    if count >= n: 
        break
    for i in range(fears[count]):
        groups[i].append(fears[i])
        count = count+1
    result = result+1

print(result)