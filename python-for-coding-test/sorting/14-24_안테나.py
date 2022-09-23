n = int(input()) # 집의 수 입력
houses = list(map(int,input().split()))

avg = sum(houses)/n # 평균값

antenna = houses[0]
for house in houses:
    antenna = house if abs(avg - house) < abs(avg - antenna) else antenna

print(antenna)   
