# 팁 :  원래 주려고 생각했던 돈 - (받은 등수 -1 )

n = int(input()) # 사람의 수 입력

# 팁 입력
data = []
for i in range(n):
    data.append(int(input()))

# 받을 수 있는 팁의 최대값
# 작은 값을 제일 뒤로
ascData = sorted(data, reverse=True)

result = 0
for i in range(n):
    result += ascData[i] - i if ascData[i] - i >= 0 else 0

print(result)