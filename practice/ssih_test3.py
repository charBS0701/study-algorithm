# 반복된 숫자 없애기
data = [10,5,6,7,10,2,5,8]
result = []

for x in data: # 결과 리스트에 없으면 추가
    if not x in result:
        result.append(x)
    
print(result)