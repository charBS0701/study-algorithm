# 개미 전사는 일직선의 식량창고를 선택적으로 약탈한다.
# 메뚜기 정찰병은 서로 인접한 식량창고가 공격받으면 알아챈다.
 
n = int(input()) # 식량창고 개수 입력
data = list(map(int,input().split())) # 창고당 식량 수 입력

# DP테이블 초기화
d = [0 for _ in range(100)] # [0] * 100

# DP 진행(보텀업)
d[0] = data[0]
d[1] = max(data[0], data[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + data[i])

# 계산된 출력 결과
print(d[n-1])

