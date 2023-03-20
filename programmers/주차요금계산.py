# 주차 요금 계산
# https://campus.programmers.co.kr/tryouts/72366/challenges?language=python3
# [180, 5000, 10, 600]	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	[14600, 34400, 5000]
# [120, 0, 60, 591]	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	[0, 591]

import collections
import math

def timeCalc(timeString):
    time = list(map(int, timeString.split(":")))
    minutes = time[0]*60 + time[1]
    return minutes
    
def solution(fees, records):
    answer = []
    parking_time = collections.defaultdict(int)
    parking_in = collections.defaultdict(bool)    
    total_time = collections.defaultdict(int)    
    parking_fee = {}
    
    for x in records:
        time, car_number, inOrOut = x.split()
        if inOrOut == "IN":
            parking_in[car_number] = True
            parking_time[car_number] = timeCalc(time)
        elif inOrOut == "OUT":
            parking_in[car_number] = False
            during_time = timeCalc(time)-parking_time[car_number]
            parking_time[car_number] = 0
            total_time[car_number] += during_time
    
    # 안 나간차 처리
    for car_number in parking_in.keys():
        if parking_in[car_number] == True:
            during_time = timeCalc("23:59") - parking_time[car_number]
            total_time[car_number] += during_time
    
    # 요금 계산
    for car_number in parking_in.keys():
        during_time = total_time[car_number] - fees[0] # 기본시간 빼기
        if during_time <= 0: # 기본시간보다 적으면 기본시간 요금
            parking_fee[car_number] = fees[1]
            continue
        during_time = math.ceil(during_time / fees[2]) # 기본시간으로 나누기
        fee = fees[1] + fees[3] * during_time
        parking_fee[car_number] = fee 
    
    parking_fee = sorted(parking_fee.items(), key=lambda x: x[0]) # 차량번호가 낮은 것부터 정렬
    
    for car_number, fee in parking_fee:
        answer.append(fee)
    
    
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))