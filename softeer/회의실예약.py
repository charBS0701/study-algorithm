# M개의 회의에 대한 정보가 주어지면
# 회의실별로 비어 있는 시간대를 정리해 출력하는 프로그램
# N개의 회의실이 있다. 방이름들은 알파벳 소문자
import sys

n, m = map(int,input().split()) # n개의 회의실, m개의 예약된 회의
rooms = []
availableHours = {}

for _ in range(n):
    room = input() # 회의실 이름 입력
    rooms.append(room)
    availableHours[room] = list(range(9,18))
    
for i in range(m):
    r, s, t = input().split() # 회의실이름, 시작시각, 종료시각 입력
    s = int(s)
    t = int(t)
    for i in range(s,t):
        availableHours[r].remove(i)

# 회의실 이름 오름차순으로 회의실 정보 출력
availableHours = dict(sorted(availableHours.items()))
print(availableHours)
# Room {회의실이름}:
# {연속된시간} available:
# 시간-시간
# ...
# -----
for key, value in availableHours.items():
    print("Room {}:".format(key))
    if value == []:
        print("Not available")
    else:
        count = 0
        times = []


    
    print("-----")