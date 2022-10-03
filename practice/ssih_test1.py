# 평균속도가 넘는 횟수 카운트 (시간,이동거리)
data1 = [[1,60],[3,180],[5,350],[8,470],[11,700]]
data2 = [[3,200],[5,300],[9,540]]

def overspeed_count(data, limit_speed):
    count = 0
    for i in range(len(data)):
        if i == 0: # 첫번째 원소일 때
            if data[0][1]/data[0][0] > limit_speed: # 속도위반 체크
                count = count+1
        # 첫번째 원소가 이닐때는 이전 원소를 빼서 제한속도 체크
        elif (data[i][1]-data[i-1][1]) / (data[i][0]-data[i-1][0]) > limit_speed: 
            count = count+1

    return count

print(overspeed_count(data1,60))
print(overspeed_count(data2,60))
