# 돌 n개가 있다 턴을 번갈아가며 돌을 가져가며
# 돌은 1개 또는 3개 가져갈 수 있다
# 마지막 돌을 가져가는 사람이 이긴다
# 이기는 사람을 구하라, 상근이가 먼저 시작

n = int(input()) # 돌의 수 입력

# dp테이블 입력
dt = [0] * 1001

dt[1] = "SK"
dt[2] = dt[1]+"CY"
dt[3] = "SK"

for i in range(4, 1000):
    # 더하기 수가 제일 작은것
    dt[i] = dt[i-1] + "CY" if dt[i-1][-2:] == "SK" else "SK"

print(dt[n[-2:]]) # 뒤에서 2개 문자열 출력