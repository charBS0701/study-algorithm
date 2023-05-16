# M개의 회의에 대한 정보가 주어지면
# 회의실별로 비어 있는 시간대를 정리해 출력하는 프로그램
# N개의 회의실이 있다. 방이름들은 알파벳 소문자

# 입력예제1
# 3 7
# grandeur
# avante
# sonata
# sonata 14 16
# grandeur 11 12
# avante 15 18
# sonata 10 11
# avante 9 12
# grandeur 16 18
# avante 12 15

# 출력예제1
# Room avante:
# Not available
# -----
# Room grandeur:
# 2 available:
# 09-11
# 12-16
# -----
# Room sonata:
# 3 available:
# 09-10
# 11-14
# 16-18

n, m = map(int,input().split()) # n개의 회의실, m개의 예약된 회의
rooms = {}

for _ in range(n):
    room = input() # 회의실 이름 입력
    rooms[room] = [0]*18+[1]   # 예약시간 초기화
    
for i in range(m):
    r, s, t = input().split() # 회의실이름, 시작시각, 종료시각 입력
    s = int(s)
    t = int(t)
    for i in range(s,t):
        rooms[r][i] = 1


# 회의실 이름 오름차순으로 회의실 정보 출력
rooms = dict(sorted(rooms.items()))

for index, room in enumerate(rooms):
    print(f'Room {room}:')
    times = []
    current = 1
    for i in range(9,19):
        if current == 1 and rooms[room][i]==0:
            start = i
            current = 0
        elif current == 0 and rooms[room][i] == 1:
            end = i
            current = 1
            times.append([start,end])
    # if current == 0:
    #     times.append([start,18])

    if len(times) == 0:
        print('Not available')
    else:
        print(f'{len(times)} available:')
        for x in times:
            print(f'{x[0]:02d}-{x[1]}')
    
    # 구분선
    if index != len(rooms)-1:
        print('-----')